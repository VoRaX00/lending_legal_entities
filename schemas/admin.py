from pydantic import BaseModel


class Administrator(BaseModel):
    email: str
    login: str

    model_config = {
        "from_attributes": True
    }