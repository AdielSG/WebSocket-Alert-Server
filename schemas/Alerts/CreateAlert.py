from pydantic import BaseModel

class CreateAlert(BaseModel):
    message:str
    location:str
