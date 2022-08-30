from fastapi import APIRouter

user_router = APIRouter()

@user_router.get('teste')
async def teste():
    return {"message": "user router working"}