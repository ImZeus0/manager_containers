from passlib.context import CryptContext
from jose import jwt

import datetime

ACCESS_TOKEN_EXPIRE = 720
ALGORITHM = 'HS256'
SECRET_KEY_TOKEN= 'be581a81692a77c12099445310633963f27c636b603a7a4dd4544047a7ce550d'


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_access_token(data:dict) -> dict:
    to_encode = data.copy()
    date = datetime.datetime.utcnow()+datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    to_encode.update({'exp':date})
    access_token = jwt.encode(to_encode,SECRET_KEY_TOKEN,algorithm=ALGORITHM)
    return {'access_token': access_token}