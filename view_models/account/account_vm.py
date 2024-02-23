from services import account_service
from view_models.base_vm import  ViewModelBase
from fastapi.requests import Request
from data_models.user import User
from typing import Optional


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user: Optional[User] = None

    async def load(self):
        self.user = await account_service.get_user_by_id(self.user_id)