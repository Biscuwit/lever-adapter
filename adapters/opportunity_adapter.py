from typing import Optional
from yarl import URL
from adapters.lever_adapter import LeverAdapter


class OpportunityAdapter:
	def __init__(self, api_key: str, endpoint_base_url="/opportunities"):
		self._api_key = api_key
		self.lever_adapter = LeverAdapter(base_url='https://api.lever.co/v1', api_key=self._api_key)
		self.endpoint_base_url = endpoint_base_url

	async def __aenter__(self) -> "OpportunityAdapter":
		return self

	async def __aexit__(self, *args) -> Optional[bool]:
		await self.lever_adapter.session.close()
		return None

	async def get_opportunity(self, opportunity_id: str):
		url = URL(self.lever_adapter.base_url).with_path(f'{self.endpoint_base_url}/{opportunity_id}')
		return await self.lever_adapter.get_data_from_endpoint(url)

	async def get_opportunities(self, limit: int):
		url = URL(self.lever_adapter.base_url).with_path(f'{self.endpoint_base_url}').with_query({'limit': limit})
		return await self.lever_adapter.get_data_from_endpoint(url)

	async def get_all_opportunities(self, params: Optional[list[dict]] = None):
		url = URL(self.lever_adapter.base_url).with_path(f'{self.endpoint_base_url}').with_query(
			params)
		return await self.lever_adapter.get_all_data_from_endpoint(url)

	async def get_deleted_opportunities(self, params: Optional[list[dict]] = None):
		url = URL(self.lever_adapter.base_url).with_path(f'{self.endpoint_base_url}/deleted').with_query(params)
		return await self.lever_adapter.get_all_data_from_endpoint(url)

	async def create_opportunity(self, payload: dict, parse: bool = False, perform_as_posting_owner: bool = False):
		params = {'perform_as': self.lever_adapter.automation_user_id}
		if parse:
			params['parse'] = parse
		if perform_as_posting_owner:
			params['perform_as_posting_owner'] = perform_as_posting_owner
		url = URL(self.lever_adapter.base_url).with_path(f'{self.endpoint_base_url}').with_query(params)
		return await self.lever_adapter.post_data_to_endpoint(url, data=payload)

	async def update_opportunity_stage(self, opportunity_id, stage):
		json = {'stage': stage}
		params: dict = {'perform_as': self.lever_adapter.automation_user_id}
		url = URL(
			self.lever_adapter.base_url) \
			.with_path(f'{self.endpoint_base_url}/{opportunity_id}/stage').with_query(params)
		return await self.lever_adapter.put_data_to_endpoint(url, body=json)

	async def update_opportunity_archived_state(
			self, opportunity_id, reason, clean_interviews=False, requisition_id=None
	):
		json = {
			'reason': reason,
			'cleanInterviews': clean_interviews
		}
		if requisition_id:
			json['requisitionID'] = requisition_id
		params: dict = {'perform_as': self.lever_adapter.automation_user_id}
		url = URL(
			self.lever_adapter.base_url) \
			.with_path(f'{self.endpoint_base_url}/{opportunity_id}/stage').with_query(params)
		return await self.lever_adapter.put_data_to_endpoint(url, body=json)

	async def _update_opportunity(self, opportunity_id: str, endpoint: str, payload: dict):
		params: dict = {'perform_as': self.lever_adapter.automation_user_id}
		url = URL(
			self.lever_adapter.base_url) \
			.with_path(f'{self.endpoint_base_url}/{opportunity_id}/{endpoint}').with_query(params)
		return await self.lever_adapter.put_data_to_endpoint(url, body=payload)

	async def add_opportunity_links(self, opportunity_id, links: list):
		json = {'links': links}
		return await self._update_opportunity(opportunity_id, "addLinks", json)

	async def remove_opportunity_links(self, opportunity_id, links: list):
		json = {'links': links}
		return await self._update_opportunity(opportunity_id, "removeLinks", json)

	async def add_opportunity_tags(self, opportunity_id, tags: list):
		json = {'tags': tags}
		return await self._update_opportunity(opportunity_id, "addLinks", json)

	async def remove_opportunity_tags(self, opportunity_id, tags: list):
		json = {'tags': tags}
		return await self._update_opportunity(opportunity_id, "removeLinks", json)

	async def add_opportunity_sources(self, opportunity_id, sources: list):
		json = {'sources': sources}
		return await self._update_opportunity(opportunity_id, "addLinks", json)

	async def remove_opportunity_sources(self, opportunity_id, sources: list):
		json = {'sources': sources}
		return await self._update_opportunity(opportunity_id, "removeLinks", json)
