import logging
import requests
import pprint

logger = logging.getLogger()

def get_contracts():

    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    # pprint.pprint(response_object.json())
    # print(response_object.status_code, response_object.json())

    contracts = []

    for contract in response_object.json()["symbols"]:

        contracts.append(contract["pair"])

    return contracts

print(get_contracts())