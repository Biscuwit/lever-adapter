from types import TracebackType
import backoff
import aiohttp
import asyncio
from aiohttp import BasicAuth
from yarl import URL
from typing import Optional, Type, Any


class LeverAdapter:
    def __int__(self, base_url: str, api_key: str, automation_user_id: str):
        self.base_url: str = base_url
        self.api_key: str = api_key
        self.automation_user_id: str = automation_user_id
        self.session = aiohttp.ClientSession(auth=BasicAuth(self.api_key), raise_for_status=True)

    async def __aenter__(self) -> "LeverAdapter":
        return self

    async def __aexit__(self, *args) -> Optional[bool]:
        await self.close()
        return None

    @property
    def base_url(self):
        return self.base_url

    @property
    def automation_user_id(self):
        return self.automation_user_id

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def get_data_from_endpoint(self, url: URL):
        async with self.session.get(url) as response:
            ret = await response.json()
            return ret

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    async def get_all_data_from_endpoint(self, url: URL):
        has_next = False
        result = []
        while has_next:
            async with self.session.get(url) as response:
                ret = await response.json()
                result += ret['data']
                has_next = ret.get('hasNext')
        return result

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    def post_data_to_endpoint(self, url: URL, json: Optional[dict], data: Any):
        with self.session.post(url, json=json, data=data) as response:
            ret = await response.json()
            return ret

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    def put_data_to_endpoint(self, url: URL, body: Optional[dict]):
        with self.session.put(url, json=body) as response:
            ret = await response.json()
            return ret

    @backoff.on_exception(backoff.expo, aiohttp.ClientError, max_tries=5)
    def delete_data_on_endpoint(self, url: URL):
        with self.session.delete(url) as response:
            ret = await response.json()
            return ret
