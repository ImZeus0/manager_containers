from pydantic import BaseModel

class Token(BaseModel):
    access_token : str
    token_type : str

class Settings(BaseModel):
    authjwt_secret_key: str = 'be581a81692a77c12099445310633963f27c636b603a7a4dd4544047a7ce550d'

