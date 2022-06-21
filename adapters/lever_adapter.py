from types import TracebackType
import backoff
import aiohttp
import asyncio
from aiohttp import BasicAuth
from yarl import URL
from typing import Optional, Type, Any


class LeverAdapter:
    def __init__(self, base_url: str, api_key: str, automation_user_id: str = None):
        self.base_url: str = base_url
        self.api_key: str = api_key
        self.automation_user_id: Optional[str] = automation_user_id
        self.session = aiohttp.ClientSession(auth=BasicAuth(self.api_key), raise_for_status=True)

    async def __aenter__(self) -> "LeverAdapter":
        return self

    async def __aexit__(self, *args) -> Optional[bool]:
        await self.session.close()
        return None

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def get_data_from_endpoint(self, url: URL):
        async with self.session.get(url) as response:
            return await response.json()

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def get_all_data_from_endpoint(self, url: URL):
        result = []
        while True:
            async with self.session.get(url) as response:
                print(f'Making request with: {url}')
                res = await response.json()
                result += res['data']
                if not res.get('hasNext'):
                    break
                url = url.update_query({'offset': res.get('next')})
        return result

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def post_data_to_endpoint(self, url: URL, json: Optional[dict], data: Any):
        async with self.session.post(url, json=json, data=data) as response:
            return await response.json()

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def put_data_to_endpoint(self, url: URL, body: Optional[dict]):
        async with self.session.put(url, json=body) as response:
            return await response.json()

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def delete_data_on_endpoint(self, url: URL):
        async with self.session.delete(url) as response:
            return await response.json()
