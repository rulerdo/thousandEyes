import requests
import json
import os


def get_bearer_token():

    BEARER_TOKEN = os.environ.get("TE_BEARER_TOKEN")

    if not BEARER_TOKEN:
        BEARER_TOKEN = input('Please provide the TE bearer token')

    return BEARER_TOKEN


def get_account_group_id(bearerToken: str, pattern: str) -> int:

    url = "https://api.thousandeyes.com/v6/account-groups.json"

    payload={}
    headers = {
      'Accept': 'application/json',
      'Authorization': f'Bearer {bearerToken}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    for account in response.json()["accountGroups"]:

        accountID = 0
        if pattern.lower() in account["accountGroupName"].lower():
            accountID = account["aid"]

    return accountID


def get_all_endpoint_tests(bearerToken: str, accountID: str) -> dict:

    url = f"https://api.thousandeyes.com/v6/endpoint-tests.json?aid={accountID}"

    payload = {}
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {bearerToken}',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def create_endpoint_test(bearerToken: str, accountID: str, testname: str, servername: str) -> dict:

    url = f"https://api.thousandeyes.com/v6/endpoint-tests/agent-to-server/new.json?aid={accountID}"

    test_template = {
    "testName": testname,
    "interval": 300,
    "serverName": servername,
    "port": 443,
    "protocol": "PREFER_TCP",
    "networkMeasurements": 1,
    "pathtraceInSession": True,
    "tcpProbeMode": "AUTO",
    "agentSelectorType": "ANY_AGENT",
    "agentIds": [],
    "labelIds": [],
    "maxMachines": 25
    }

    payload = json.dumps(test_template)
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {bearerToken}',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()
