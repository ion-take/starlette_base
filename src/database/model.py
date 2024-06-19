
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
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20))
    phone: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(90), nullable=False)
    access: Mapped['Access'] = relationship(back_populates='user')
    control: Mapped['Control'] = relationship(back_populates='user')


    def __repr__(self)->str:
        return self.name 
    



class Access(Base):
    __tablename__ = 'access'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    is_block: Mapped[bool] = mapped_column(Boolean, default=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user._id'), nullable=False)
    user: Mapped['User'] = relationship(back_populates='access')

    def __repr__(self):
        return f"""
        user_id: {self.user_id}
        is_active: {self.is_active}
        is_block: {self.is_block}
        """


class Provider(Base):

    __tablename__ = 'provider'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(15))
    description: Mapped[str] = mapped_column(Text)    

    control: Mapped['Control'] = relationship(back_populates='provider')

    def __repr__(self):
        return f"""
        name: {self.name}
        phone: {self.phone}
        description: {self.description}
        """


class Location(Base):
    __tablename__ = 'location'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(5), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    control: Mapped[List['Control']] = relationship(back_populates='location')

    def  __repr__(self):
        return ''





class Category(Base):
    __tablename__ = 'category'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(15), nullable=False)
    desctiption: Mapped[str] = mapped_column(Text)
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey('category._id'), nullable=True)
    parent: Mapped[List['Category']] = relationship(remote_side=[_id])
    
    header_img: Mapped[ImageField] = mapped_column(ImageField(
        upload_storage='category', thumbnail_size=(1500,500), validators=[SizeValidator(max_size="10M")])
    )
    small_img: Mapped[ImageField] = mapped_column(ImageField(
        upload_storage='category', thumbnail_size=(500,500), validators=[SizeValidator(max_size="10M")])
    )


    def __repr__(self):
        return ''



Product_Variant = Table(
    "product_variant",
    Base.metadata,
    Column("current", Integer, ForeignKey("product._id"), primary_key=True),
    Column("variant", Integer, ForeignKey("product._id"), primary_key=True),
)



class Product(Base):
    __tablename__ = 'product'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    price: Mapped[float] = mapped_column(Float)
    qrcode: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    
    current: Mapped[List['Product']] = relationship(
        "Product",
        secondary=Product_Variant,
        primaryjoin=_id == Product_Variant.c.current,
        secondaryjoin=_id == Product_Variant.c.variant,
        back_populates="variant"
    )
    variant: Mapped[List['Product']] = relationship(
        "Product",
        secondary=Product_Variant,
        primaryjoin=_id == Product_Variant.c.variant,
        secondaryjoin=_id == Product_Variant.c.current,
        back_populates="current"
    )
    description: Mapped[str] = mapped_column(Text)
    control: Mapped[List['Control']] = relationship(back_populates='product')
    offerd: Mapped['offerd'] = relationship(back_populates='product')
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category._id'))
    category: Mapped[List['Category']] = relationship(back_populates='product')
    state: Mapped['ProductState'] = relationship(back_populates='product')

    def __repr__(self):
        return ''

    
class Control(Base):
    
    __tablename__ = 'control'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)
    received_at: Mapped[datetime.datetime] = mapped_column(default_server=func.now())
    expired_at: Mapped[datetime.datetime] = mapped_column(default=(datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=50)))
    cuantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    user: Mapped['User'] = relationship(back_populates='control')
    provider: Mapped['Provider'] = relationship(back_populates='control')
    location: Mapped['Location'] = relationship(back_populates='control')

    def __repr__(self):
        return ''



class Offerd(Base):
    __tablename__ = 'offerd'

    _id: Mapped[int] = mapped_column(Integer, primary_key=True)
    state: Mapped[bool] = mapped_column(Boolean, default=False)
    price: Mapped[float] = mapped_column(Float)

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product._id'))

    def __repr__(self):
        return ''
