from fastapi.security import OAuth2PasswordBearer
from fastapi.types import DependencyCacheKey
from jose import JWTError, jwt
from datetime import timedelta,datetime
from fastapi import Depends, HTTPException
from app.config import SECRET_KEY

Secret_key = SECRET_KEY
Token_expire_time = 30
algo = "HS256"

oauth_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)

def create_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=Token_expire_time)

    to_encode.update({"exp":expire})

    token = jwt.encode(
        to_encode,
        Secret_key,
        algorithm=algo
    )

    return token

def verify_token(token:str=Depends(oauth_scheme)):

    try:
          payload = jwt.decode(token,Secret_key,algorithms=[algo])

          user_id = payload.get("sub")

          if user_id is None:
               raise HTTPException(
                    status_code=401,
                    details="Invalid Token"
               )
          return int(user_id)
    
    except Exception as e:
         print("JWT ERROR : ",e)

         raise HTTPException(
              status_code = 401,
              detail=str(e)
         )

