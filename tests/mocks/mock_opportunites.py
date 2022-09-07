
def example_opportunity_data() -> dict:
	return {
			"id": "250d8f03-738a-4bba-a671-8a3d73477145",
			"name": "Shane Smith",
			"headline": "Brickly LLC, Vandelay Industries, Inc, Central Perk",
			"contact": "7f23e772-f2cb-4ebb-b33f-54b872999992",
			"emails": [
				"shane@exampleq3.com"
			],
			"phones": [
				{
					"value": "(123) 456-7891"
				}
			],
			"confidentiality": "non-confidential",
			"location": "Oakland",
			"links": [
				"indeed.com/r/Shane-Smith/0b7c87f6b246d2bc"
			],
			"createdAt": 1407460071043,
			"updatedAt": 1407460080914,
			"lastInteractionAt": 1417588008760,
			"lastAdvancedAt": 1417587916150,
			"snoozedUntil": 1505971500000,
			"archived": None,
			"stage": "00922a60-7c15-422b-b086-f62000824fd7",
			"stageChanges": [
				{
					"toStageId": "00922a60-7c15-422b-b086-f62000824fd7",
					"toStageIndex": 1,
					"userId": "df0adaa6-172c-4cd6-8520-49b203660fe1",
					"updatedAt": 1407460071043
				}
			],
			"owner": "df0adaa6-172c-4cd6-8520-49b203660fe1",
			"tags": [
				"San Francisco",
				"Full-time",
				"Support",
				"Customer Success",
				"Customer Success Manager"
			],
			"sources": [
				"linkedin"
			],
			"origin": "sourced",
			"sourcedBy": "df0adaa6-172c-4cd6-8520-49b203660fe1",
			"applications": [
				"cdb4ff13-f7aa-49b0-b6ec-eb4617009cfa"
			],
			"resume": None,
			"followers": [
				"df0adaa6-172c-4cd6-8520-49b203660fe1",
				"ecdb6670-d9f3-4b87-8267-1cde26d1bc42",
				"022d6639-1333-419b-9635-31f93015335f"
			],
			"urls": {
				"list": "https://hire.lever.co/candidates",
				"show": "https://hire.lever.co/candidates/250d8f03-738a-4bba-a671-8a3d73477145"
			},
			"dataProtection": {
				"store": {
					"allowed": True,
					"expiresAt": 1522540800000
				},
				"contact": {
					"allowed": False,
					"expiresAt": None
				}
			},
			"isAnonymized": False
		}


def opportunity_data_with_missing_keys() -> dict:
	return {
		"id": "250d8f03-738a-4bba-a671-8a3d73477145",
		"name": "Shane Smith",
		"headline": "Brickly LLC, Vandelay Industries, Inc, Central Perk",
		"contact": "7f23e772-f2cb-4ebb-b33f-54b872999992",
	}


def opportunity_data_with_wrong_value_types() -> dict:
	return {
		"id": "250d8f03-738a-4bba-a671-8a3d73477145",
		"name": "Shane Smith",
		"headline": "Brickly LLC, Vandelay Industries, Inc, Central Perk",
		"contact": "7f23e772-f2cb-4ebb-b33f-54b872999992",
		"emails": [
			"shane@exampleq3.com"
		],
		"phones": [
			{
				"value": "(123) 456-7891"
			}
		],
		"confidentiality": "non-confidential",
		"location": "Oakland",
		"links": [
			"indeed.com/r/Shane-Smith/0b7c87f6b246d2bc"
		],
		"createdAt": "1407460071043",
		"updatedAt": 1407460080914,
		"lastInteractionAt": 1417588008760,
		"lastAdvancedAt": 1417587916150,
		"snoozedUntil": 1505971500000,
		"archivedAt": None,
		"archiveReason": None,
		"stage": "00922a60-7c15-422b-b086-f62000824fd7",
		"stageChanges": [
			{
				"toStageId": "00922a60-7c15-422b-b086-f62000824fd7",
				"toStageIndex": 1,
				"userId": "df0adaa6-172c-4cd6-8520-49b203660fe1",
				"updatedAt": 1407460071043
			}
		],
		"owner": "df0adaa6-172c-4cd6-8520-49b203660fe1",
		"tags": [
			"San Francisco",
			"Full-time",
			"Support",
			"Customer Success",
			"Customer Success Manager"
		],
		"sources": [
			"linkedin"
		],
		"origin": "sourced",
		"sourcedBy": "df0adaa6-172c-4cd6-8520-49b203660fe1",
		"applications": [
			"cdb4ff13-f7aa-49b0-b6ec-eb4617009cfa"
		],
		"resume": None,
		"followers": [
			"df0adaa6-172c-4cd6-8520-49b203660fe1",
			"ecdb6670-d9f3-4b87-8267-1cde26d1bc42",
			"022d6639-1333-419b-9635-31f93015335f"
		],
		"urls": {
			"list": "https://hire.lever.co/candidates",
			"show": "https://hire.lever.co/candidates/250d8f03-738a-4bba-a671-8a3d73477145"
		},
		"dataProtection": {
			"store": {
				"allowed": True,
				"expiresAt": 1522540800000
			},
			"contact": {
				"allowed": False,
				"expiresAt": None
			}
		},
		"isAnonymized": False
	}
