from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly', "https://www.googleapis.com/auth/directory.readonly"]

def main():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    # results = service.people().listDirectoryPeople(
    #     # resourceName='people/me',
    #     readMask='names,emailAddresses,phoneNumbers,organizations',
    #     # sources='DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE',
    #     sources='DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE',
    #     pageSize=200,
    #     # personFields='names'
    # ).execute()
    # connections = results.get('connections', [])

    a=  service.people().get(resourceName="people/me", requestMask_includeField="." )
    a=  service.people().searchContacts(pageSize=10, query="Савчук", readMask="names,emailAddresses").execute()
    # print(a.headers)
    # print(dir(a))
    # print(a)
    # print(a.execute)

    for person in a.get("results"):
        names = person.get("person").get('names', [])
        if names:
            name = names[0].get('displayName')
            print(name)

if __name__ == '__main__':
    main()