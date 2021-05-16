from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar', "https://www.googleapis.com/auth/contacts.readonly"]


def get_calendars():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2021-05-06T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2021-05-06T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    # event = service.events().insert(calendarId='primary', body=event).execute()

    calendar_list_entry = service.calendarList().get(
        calendarId="ucu.edu.ua_2d3838313332353630373933@resource.calendar.google.com").execute()
    calendar_list_entry = service.calendarList().get(
        calendarId="addressbook#contacts@group.v.calendar.google.com").execute()
    calendar_list_entry = service.calendarList().list().execute()
    for i in [i for i in calendar_list_entry['items']]:
        print(i)

    input()
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            print(calendar_list_entry['id'])
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break


def PrintAllContacts(gd_client):
    feed = gd_client.GetContacts()
    for i, entry in enumerate(feed.entry):
        print('\n%s %s' % (i + 1, entry.name.full_name.text))
        if entry.content:
            print('    %s' % (entry.content.text))
        # Display the primary email address for the contact.
        for email in entry.email:
            if email.primary and email.primary == 'true':
                print('    %s' % (email.address))
        # Show the contact groups that this contact is a member of.
        for group in entry.group_membership_info:
            print('    Member of group: %s' % (group.href))
        # Display extended properties.
        for extended_property in entry.extended_property:
            if extended_property.value:
                value = extended_property.value
            else:
                value = extended_property.GetXmlBlob()
            print('    Extended Property - %s: %s' % (extended_property.name, value))


if __name__ == '__main__':
    CLIENT_ID = "467475306130-la5grpe26apbqqunlbegdqro11etq198.apps.googleusercontent.com"
    CLIENT_SECRET = "DndEXTZKH-ZrciHCDNXCKlBQ"
    ACCESS_TOKEN = "ya29.a0AfH6SMDUjNg8Z6-v9Ghe12rfVRv_Jw77NwQ10QjvVIWVeNitCZFzGxwSU0mhN1CfFac5LIJKD1DKYDvvutbfhXqp4vAh5Tvwui7a7c2q8DX4mGSKlUZSpdBW9I_avUZ6-hjXikRXWaZ0zgTVeD9ffiBx8yxsQg"
    CREATE_ROUTE = 'https://www.google.com/m8/feeds/contacts/yewgeenn@ucu.edu.ua/full'
    FULL_PATH = CREATE_ROUTE + '?access_token=' + ACCESS_TOKEN

    import requests
    r = requests.get(FULL_PATH)
    print(r.text)

    # ...
    # gd_client = gdata.contacts.client.ContactsClient(source='UCU APP API')
    # print(gd_client)
    # PrintAllContacts(gd_client)
# get_calendars()
