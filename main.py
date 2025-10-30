from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from routes.users import user_router
from routes.events import event_router
import uvicorn

from contextlib import asynccontextmanager

from database.connection import Settings

origins = ["*"]

shared_resources = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

#Register routes

settings = Settings()

app.include_router(user_router, prefix="/user")
app.include_router(event_router,prefix="/event")


#@app.on_event("startup")
#async def init_db():
#    await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload =True)