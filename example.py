import asyncio
import logging
import os

from dotenv import load_dotenv

from adapters.opportunity_adapter import OpportunityAdapter
from models.opportunity import Opportunity

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")
logger = logging.getLogger(__name__)
load_dotenv()
api_key = os.environ.get('LEVER_API_KEY')


async def main():
	logger.info("Starting Example app")
	async with OpportunityAdapter(api_key=api_key) as api:
		opps: list[Opportunity] = await api.get_opportunities(limit=50)
		for opp in opps:
			logger.info(opp.name)


if __name__ == "__main__":
	asyncio.run(main())
