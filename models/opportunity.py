from dataclasses import dataclass
from typing import Optional

import dacite


@dataclass
class Opportunity:
	id: str
	name: str
	headline: str
	contact: str
	stage: str
	stageChanges: Optional[list[dict]]
	confidentiality: str
	location: str
	phones: list[dict]
	emails: list[str]
	links: list[str]
	resume: Optional[bool]
	archivedAt: Optional[int]
	archiveReason: Optional[str]
	tags: list[str]
	sources: list[str]
	sourcedBy: Optional[str]
	origin: str
	owner: str
	followers: list[str]
	applications: list[str]
	createdAt: int
	updatedAt: int
	lastInteractionAt: int
	lastAdvancedAt: int
	snoozedUntil: Optional[int]
	urls: dict
	dataProtection: Optional[dict]
	isAnonymized: bool
	deletedAt: Optional[int]
	deletedBy: Optional[str]

	@staticmethod
	def from_dict(data):
		return dacite.from_dict(Opportunity, data)
