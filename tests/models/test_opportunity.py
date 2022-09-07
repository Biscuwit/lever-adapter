import pytest
from dacite import MissingValueError, WrongTypeError

from models.opportunity import Opportunity
from tests.mocks import mock_opportunites


class TestOpportunity:
	example_opportunity = mock_opportunites.example_opportunity_data()
	opportunity_data_with_missing_keys = mock_opportunites.opportunity_data_with_missing_keys()
	opportunity_data_with_bad_value_types = mock_opportunites.opportunity_data_with_wrong_value_types()

	def test_from_dict(self):
		opp: Opportunity = Opportunity.from_dict(self.example_opportunity)
		assert isinstance(opp, Opportunity)

	def test_from_dict_with_missing_keys(self):
		with pytest.raises(MissingValueError) as err:
			opp: Opportunity = Opportunity.from_dict(self.opportunity_data_with_missing_keys)

	def test_from_dict_with_bad_value_types(self):
		with pytest.raises(WrongTypeError):
			opp: Opportunity = Opportunity.from_dict(self.opportunity_data_with_bad_value_types)

