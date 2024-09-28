from sqlalchemy import VARCHAR, Column

from core.db import DeclarativeBase
from models.base import BaseModelMixin


class TelegramUser(BaseModelMixin, DeclarativeBase):
    __tablename__ = "tg_users"

    telegram_id: str = Column(VARCHAR(255), nullable=False, index=True, unique=True)
    username: str | None = Column(VARCHAR(255))
    mention: str | None = Column(VARCHAR(255))
    full_name: str | None = Column(VARCHAR(255))
    phone: str | None = Column(VARCHAR(255))
