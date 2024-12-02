# copy and paste from
# https://stackoverflow.com/questions/76805337/python-send-email-using-graph-api-and-office365-rest-python-client
# see our own PHPGraphMailer for details

import msal
import requests

dict_ = {'client_id': 'appId', 'secret': 'secret', 'tenant_id': 'tenantId'}


def acquire_token():
    authority_url = f'https://login.microsoftonline.com/{dict_["tenant_id"]}'
    app = msal.ConfidentialClientApplication(
        authority=authority_url,
        client_id=dict_["client_id"],
        client_credential=dict_["secret"]
    )
    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return token


def send_email():
    endpoint = f'https://graph.microsoft.com/v1.0/users/userId/sendMail'
    toUserEmail = "sri@xxxxxxxxxx.onmicrosoft.com"
    email_msg = {'Message': {'Subject': "Meet for lunch?",
                             'Body': {'ContentType': 'Text', 'Content': "The new cafeteria is open."},
                             'ToRecipients': [{'EmailAddress': {'Address': toUserEmail}}]
                             },
                 'SaveToSentItems': 'true'}

    r = requests.post(endpoint, headers={'Authorization': 'Bearer ' + result['access_token']}, json=email_msg)
    if r.ok:
        print('Sent email successfully')
        return True
    else:
        print(r.json())
        return False


result = acquire_token()

if "access_token" in result:
    print("Access token created.", result["access_token"])

if "access_token" in result:
    sendMail()
