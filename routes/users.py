from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

from database.connection import Database

user_router = APIRouter(tags=["User"])

user_database = Database(User)

users = {}

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    users[data.email] = data
    return{
        "message":"User successfully registered"
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_onde(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if user_exist.password == user.password:
        return {
            "message": "User signed in successfully"
        }
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed"
    )
    