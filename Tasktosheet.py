import os

def main():
    refresh_token = os.getenv('GOOGLE_TASKS_REFRESH_TOKEN')
    client_id = os.getenv('GOOGLE_TASKS_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_TASKS_CLIENT_SECRET')

    print("GOOGLE_TASKS_REFRESH_TOKEN:", refresh_token)
    print("GOOGLE_TASKS_CLIENT_ID:", client_id)
    print("GOOGLE_TASKS_CLIENT_SECRET:", client_secret)

if __name__ == "__main__":
    main()
