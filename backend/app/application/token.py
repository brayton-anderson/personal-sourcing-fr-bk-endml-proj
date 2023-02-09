from datetime import datetime, timedelta
from jose import JWTError, jwt
from application import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception


#Gooogle Custom Search API
#API = "AIzaSyCDuGaIhulAulTrBbSmCX_Gj3p5xAMvhhQ"
#CX = "988531739927-2rhf9cak2prr573tgeo0pnnfalovqd8l.apps.googleusercontent.com"

#Github API
#Client Secret: 2be887d85ae26258fd533ba2e8a54631da6f520e
#Client ID: Iv1.5a66d2b1db3cc008
#App ID: 288407

#LinkedIn API
#Client Secret: zvIkzLBTNhi7tEo0
#Client ID: 77dcxcv8614d11

