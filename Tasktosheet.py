import os
import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
TASKS_SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]
SHEETS_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Your Google Sheets spreadsheet ID and range
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
RANGE_NAME = 'Sheet1'  # Modify according to your sheet

def get_tasks(credentials):
    """Retrieve pending tasks from Google Tasks."""
    service = build("tasks", "v1", credentials=credentials)
    results = service.tasks().list(tasklist='@default').execute()
    tasks = results.get("items", [])
    return tasks

def write_to_sheet(credentials, tasks):
    """Write tasks to Google Sheet."""
    creds = Credentials.from_authorized_user_file("token.json", SHEETS_SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(RANGE_NAME)
    for task in tasks:
        sheet.append_row([task['title'], task['id']])

def main():
    """Main function to retrieve tasks and write to sheet."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", TASKS_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "tasks_credentials.json", TASKS_SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        tasks = get_tasks(creds)
        write_to_sheet(creds, tasks)
        print("Tasks successfully written to Google Sheet.")
    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()
