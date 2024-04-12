import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def test_google_api():
    # Ensure all required environment variables are set
    required_env_vars = ['GOOGLE_TASKS_REFRESH_TOKEN', 'GOOGLE_TASKS_CLIENT_ID', 'GOOGLE_TASKS_CLIENT_SECRET']
    for env_var in required_env_vars:
        if env_var not in os.environ:
            print(f"Error: Environment variable '{env_var}' is not set.")
            return False
    
    # Load credentials from environment variables
    creds = Credentials(
        refresh_token=os.getenv('GOOGLE_TASKS_REFRESH_TOKEN'),
        client_id=os.getenv('GOOGLE_TASKS_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_TASKS_CLIENT_SECRET')
    )
    
    try:
        # Build the Tasks API service
        service = build('tasks', 'v1', credentials=creds)

        # Test communication with the Tasks API
        tasklists = service.tasklists().list(maxResults=5).execute()
        print("Successfully retrieved task lists:")
        for tasklist in tasklists['items']:
            print(f"- {tasklist['title']} (ID: {tasklist['id']})")
        
        return True
    except Exception as e:
        print(f"Error: Failed to communicate with the Tasks API. {e}")
        return False

if __name__ == "__main__":
    test_google_api()
