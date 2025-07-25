import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/tasks"]

def get_credentials():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def get_email_body(payload):
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                return base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
    elif "body" in payload:
        return base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8")
    return ""

def main():
    creds = get_credentials()
    gmail_service = build("gmail", "v1", credentials=creds)
    tasks_service = build("tasks", "v1", credentials=creds)

    search_query = input("Enter your search query for Gmail: ")

    try:
        results = gmail_service.users().messages().list(userId="me", q=search_query).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
            return

        print(f"Found {len(messages)} messages.")

        task_lists = tasks_service.tasklists().list().execute().get("items", [])
        if not task_lists:
            print("No task lists found. Please create one in Google Tasks.")
            return

        print("Available Task Lists:")
        for i, task_list in enumerate(task_lists):
            print(f"{i + 1}. {task_list['title']}")
        
        choice = int(input("Choose a task list to add tasks to: ")) - 1
        task_list_id = task_lists[choice]["id"]

        for message in messages:
            msg = gmail_service.users().messages().get(userId="me", id=message["id"]).execute()
            
            payload = msg["payload"]
            headers = payload["headers"]
            subject = ""
            for header in headers:
                if header["name"] == "Subject":
                    subject = header["value"]
                    break
            
            body = get_email_body(payload)

            # This is where you would add your NLP logic to find action items.
            # For now, we'll just create a task with the email subject.
            print(f"\nSubject: {subject}")
            create_task = input("Create a task for this email? (yes/no): ").lower()

            if create_task == "yes":
                task = {
                    "title": subject,
                    "notes": body
                }
                tasks_service.tasks().insert(tasklist=task_list_id, body=task).execute()
                print("Task created successfully.")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
