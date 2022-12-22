from te_manager import get_bearer_token,get_account_group_id,create_endpoint_test
from pprint import pprint


if __name__ == '__main__':

    testnameList = [
        "Google",
        "Cisco",
    ]

    servernameList = [
        "google.com",
        "cisco.com",
    ]

    bearerToken = get_bearer_token()
    accountID = get_account_group_id(bearerToken,'rgomezbe')

    for testname,servername in zip(testnameList,servernameList):
        response = create_endpoint_test(bearerToken,accountID,testname,servername)
        pprint(response)
        print('')
