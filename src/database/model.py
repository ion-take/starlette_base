
from __future__ import annotations

# database models 

from typing import Any

from secrets import token_hex
import asyncio
import datetime
from typing import List
import hashlib

import enum 

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import Enum
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import Select
from sqlalchemy_file import FileField, ImageField
from sqlalchemy_file.validators import ContentTypeValidator, SizeValidator, ImageValidator


from werkzeug.security import check_password_hash

from src.settings import get_resouces_location


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    
    _id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    
    def repr(self)->str:
        return self.name 
    
    async def run_query(self, session: AsyncSession, query: Select)-> Any:
        intent = await session.execute(query)
        return intent



