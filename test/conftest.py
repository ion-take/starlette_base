

from typing import AsyncIterator
from starlette.testclient import TestClient

from src import create_app
from src.logger import logger_manager 
from src.settings import Env
from src.database.connection import create_db, drop_db
from src.database.connection import async_engine

import pytest
import httpx
import pytest_asyncio



@pytest_asyncio.fixture()
async def client() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=create_app(), base_url="http://testserver") as client:
      
        log = logger_manager('testing')
        # log.info('initializing db process')
        try:
            log.info('Creating database')
            await create_db(Env.DB_ADMINISTRATION_NAME)
            # log.info('Database created')

        except Exception as e:
            log.error(str(e))

        yield client
