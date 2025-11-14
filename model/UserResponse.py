from model.RoleResponse import RoleResponse
from config.base_response import BaseResponseModel

class UserResponse(BaseResponseModel):
    id: int
    name: str
    email: str
    active: bool
    role: RoleResponse   # nested DTO


