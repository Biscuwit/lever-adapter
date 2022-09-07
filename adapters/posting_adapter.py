from typing import Optional

from yarl import URL

from adapters.lever_adapter import LeverAdapter
from models.posting import Posting


class PostingAdapter:
	def __init__(self, api_key: str, endpoint_base_url="v1/postings"):
		self._api_key = api_key
		self.lever_adapter = LeverAdapter(base_url='https://api.lever.co', api_key=self._api_key)
		self.endpoint_base_url = endpoint_base_url

	async def __aenter__(self) -> "PostingAdapter":
		return self

	async def __aexit__(self, *args) -> Optional[bool]:
		await self.lever_adapter.session.close()
		return None

	async def get_posting(self, posting_id: str) -> Posting:
		url = URL(self.lever_adapter.base_url).with_path(f'{self.endpoint_base_url}/{posting_id}')
		response = await self.lever_adapter.get_data_from_endpoint(url)
		return Posting.from_dict(response['data'])

	async def create_posting(self, data: dict):
		params = {'perform_as': self.lever_adapter.automation_user_id}
		url = URL(self.lever_adapter.base_url).with_query(params)
		result = await self.lever_adapter.post_data_to_endpoint(url=url, data=data)
		return result

	async def update_posting(self, posting_id: str, data: dict):
		params = {'perform_as': self.lever_adapter.automation_user_id}
		url = URL(self.lever_adapter.base_url).with_path(posting_id).with_query(params)
		result = await self.lever_adapter.post_data_to_endpoint(url=url, data=data)
		return result

