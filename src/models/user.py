from sqlmodel import Field

from .base import BaseModel


class User(BaseModel, table=True):
    id: str = Field(index=True, primary_key=True, nullable=False)
    username: str | None
    mention: str | None
    full_name: str | None
    is_admin: bool = Field(default=False)
