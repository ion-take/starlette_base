
#  importing the click manager handler
import asyncclick as click
# from werkzeug.security import generate_password_hash

#  importing databse connection components 
from src.database.connection import create_db, drop_db, async_session
from src.database.model import User
from src.settings import Env
from src.logger import logger_manager

# creating a logger manager
logger = logger_manager('manage_app')


@click.group()
async def Tasks():pass    # main task object 


@click.command()
async def init_db():
    try:
        await create_db(Env.DB_ADMINISTRATION_NAME)
        logger.info('adminitration database created')

    except Exception as e:
        logger.error(str(e))


@click.command()
async def delete_db():
    try:
        await drop_db(Env.DB_ADMINISTRATION_NAME)
        logger.info('database delete')
    except Exception as e:
        logger.error(str(e))



@click.command()
async def create_user():
    async with (async_session(Env.DB_ADMINISTRATION_NAME)).begin() as session:
        try:
            await insert_user(session)
        except Exception as e:
            await session.rollback()
            logger.error(str(e))


async def insert_user(session):
    session.add_all([      
        User(name='alan@home.com'),User(name='juan@home.com'),
        User(name='maria@home.com'),User(name='juana@home.com'),
        User(name='one@home.com'),User(name='Tuew@home.com')
    ])
    await session.commit()
    logger.info('users created')


Tasks.add_command(init_db)
Tasks.add_command(delete_db)
Tasks.add_command(create_user)

if __name__=='__main__':
    Tasks()