from te_manager import get_bearer_token,get_account_group_id,get_all_endpoint_tests
from pprint import pprint


if __name__ == '__main__':

    bearerToken = get_bearer_token()
    accountID = get_account_group_id(bearerToken,'rgomezbe')
    response = get_all_endpoint_tests(bearerToken,accountID)
    pprint(response)
