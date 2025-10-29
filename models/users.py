from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List

from beanie import Document, Link

from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = None

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
            "email": "fastapi@packt.com",
            "password": "strong!!!",
            "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
    json_schema_extra = {
        "examples": [{
            "email": "fastapi@packt.com",    
            "password": "strong!!!",
            }]
        }
    )