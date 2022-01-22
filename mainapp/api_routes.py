from fastapi import APIRouter, Depends
from .schemas import UserSchema, TokenSchema
from .models import Users
from .services import create_access_token, decode_access_token


router = APIRouter()

@router.post("/create-token")
def create_token(data: UserSchema):
    user = Users.check_credentials(data.username, data.password)
    if user:
        token = create_access_token(data.username)
        return token
    return 'fail'


@router.post('/decode-token')
def decode_token(data: TokenSchema):
    result = decode_access_token(data)
    return result