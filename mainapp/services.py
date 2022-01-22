import jwt
import json
from .schemas import TokenSchema


SECRET_KEY = '1231r4r4r4'

def create_access_token(username: str) -> dict:
    encoded_jwt = jwt.encode(
        {'username': username}, key=SECRET_KEY, algorithm="HS256"
    )
    return {'token': encoded_jwt}


def decode_access_token(token_data: TokenSchema) -> bool:
    data = token_data.dict()
    token = data.get('token', None)
    if token:
        try:
            payload = jwt.decode(token, key=SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.PyJWTError:
            raise Exception("Could not to decode a token")
    return False