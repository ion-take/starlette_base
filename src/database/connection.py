

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine

from src.settings import Env

from .model import Base




#  making some batteries 

def async_engine(uri:str) -> AsyncEngine:
    #  creating a engine...
    engine: create_async_engine[AsyncEngine] = create_async_engine(generate_uri(uri))
    return engine



def async_session(uri:str) -> async_sessionmaker[AsyncSession]: 
    #  creating a session...
    session = async_sessionmaker(async_engine(uri), expire_on_commit=False) 
    return session



def generate_uri(uri:str):

    if Env.USE_MYSQL:
        uri  = Env.MYSQL_DB_URI+uri
        return uri
        
    elif Env.USE_SQLITE:
        uri = Env.SQLITE_DB_URI+uri+'.db'
        return uri

    elif Env.USE_POSTGRESS:
        uri = Env.POSGRESS_URI+uri
        return uri

    else:
        raise RuntimeError('No Database URI provided')


async def create_db(uri:str):
    #  create a new tenant database...
    async with (async_engine(uri)).begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



async def drop_db(uri:str):
    # delete the current tenant database ...
    async with (async_engine(uri)).begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
