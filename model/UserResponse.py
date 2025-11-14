from model.RoleResponse import RoleResponse
from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    active: bool
    role: RoleResponse   # nested DTO

    model_config = ConfigDict(from_attributes=True)

