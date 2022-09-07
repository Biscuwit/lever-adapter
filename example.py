import asyncio
import logging
import os

from adapters.opportunity_adapter import OpportunityAdapter
from dotenv import load_dotenv
from models.opportunity import Opportunity

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")
logger = logging.getLogger(__name__)
load_dotenv()
api_key = os.environ.get('LEVER_API_KEY')


async def main():
	logger.info("Starting Example app")
	async with OpportunityAdapter(api_key=api_key) as api:
		example_opp: Opportunity = await api.get_opportunity('ab4e3f06-94b0-41b6-a90e-752a1554acfb')
		logger.info(example_opp.name)

		params = {'limit': 100, 'archived': 'false', 'stage_id': 'lead-new'}
		opps: list[Opportunity] = await api.get_all_opportunities(params)
		logger.info(len(opps))


if __name__ == "__main__":
	asyncio.run(main())
