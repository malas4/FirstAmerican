import json
import jsonschema
from jsonschema import validate

buyer_schema = open('C://Users//Nihaan//PycharmProjects//FirstAmerican//tests//schema_buyer.json')
buyer_response = open('C://Users//Nihaan//PycharmProjects//FirstAmerican//FileD.json')
buyer_schema_data = json.load(buyer_schema)
buyer_response_data = json.load(buyer_response)

"""owner schema and response files"""
owner_schema = open('C://Users//Nihaan//PycharmProjects//FirstAmerican//schema_owner.json')
owner_response = open('C://Users//Nihaan//PycharmProjects//FirstAmerican//FileB.json')
owner_schema_data = json.load(owner_schema)
owner_response_data = json.load(owner_response)


def test_assert_valid_schema_buyer_response():
    """ Checks whether the given data matches the schema """
    try:
        validate(buyer_response_data, buyer_schema_data)
        print("json schema is valid")
    except ValueError:
        print("given json data is invalid")
        return False


def test_assert_valid_schema_owner_response():
    """ Checks whether the given data matches the schema """
    try:
        validate(owner_response_data, owner_schema_data)
        print("json schema is valid")
    except ValueError:
        print("given json data is invalid")
        return False
