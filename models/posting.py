from dataclasses import dataclass
from typing import Optional

import dacite


@dataclass
class Posting:
	id: str
	text: str
	createdAt: int
	updatedAt: Optional[int]
	state: str
	distributionChannels: list[str]
	confidentiality: str
	user: Optional[str, dict]
	owner: Optional[str, dict]
	hiringManager: Optional[str, dict]
	categories: dict
	tags: Optional[list[str]]
	content: dict
	followers: list[Optional[str, dict]]
	requisitionCodes: list[str]
	urls: dict

	@staticmethod
	def from_dict(data):
		return dacite.from_dict(Posting, data)
