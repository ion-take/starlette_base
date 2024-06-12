

from starlette import status 
import pytest



@pytest.mark.asyncio
async def test_login(client):
    resp = await client.get("/auth/login")
    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_logout(client):
    resp = await client.get("/auth/logout")
    assert resp.status_code == status.HTTP_303_SEE_OTHER
