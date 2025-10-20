from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = None

    model_config = ConfigDict(
    json_schema_extra = {
        "examples": [{
            "email": "fastapi@packt.com",    
            "password": "strong!!!",
            "username": "strong!!!",
            "events": [],
            }]
        }
    )

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