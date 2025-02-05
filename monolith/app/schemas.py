from pydantic import BaseModel, ConfigDict


class BaseAPIResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
