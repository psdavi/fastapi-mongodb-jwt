from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserAuth
from app.services.user_service import UserService
import pymongo

user_router = APIRouter()


@user_router.post('/create', summary = "Create new User")
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
        


""" @user_router.get('teste')
async def teste():
    return {"message": "user router working"} """