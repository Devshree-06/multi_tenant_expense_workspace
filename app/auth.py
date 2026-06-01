from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import timedelta,datetime


Secret_key = "224f56ba31aa8e0658ac03ecaff99dce3d49b3ceb9d1c6336d00b05c5b375f0a"
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
    
