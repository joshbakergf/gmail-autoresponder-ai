import base64
from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import GMAIL_USER_ID

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
SERVICE_ACCOUNT_FILE = 'service_account.json'
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('gmail', 'v1', credentials=creds)

def get_unread_messages():
    response = service.users().messages().list(userId=GMAIL_USER_ID, labelIds=['INBOX', 'UNREAD']).execute()
    return response.get('messages', [])

def get_message_content(msg_id):
    msg = service.users().messages().get(userId=GMAIL_USER_ID, id=msg_id, format='full').execute()
    headers = msg['payload']['headers']
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
    sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
    snippet = msg.get('snippet', '')
    message_id = next((h['value'] for h in headers if h['name'] == 'Message-ID'), '')
    thread_id = msg.get('threadId')
    return subject, sender, snippet, thread_id, message_id

def send_email_reply_in_thread(to_email, subject, body, thread_id, message_id):
    from email.mime.text import MIMEText
    from_email = "Auto Responder <you@yourdomain.com>"
    message = MIMEText(body)
    message['To'] = to_email
    message['From'] = from_email
    message['Subject'] = "Re: " + subject
    message['In-Reply-To'] = message_id
    message['References'] = message_id
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return service.users().messages().send(userId=GMAIL_USER_ID, body={'raw': raw, 'threadId': thread_id}).execute()

def apply_label(msg_id, label_name):
    label_id = get_or_create_label(label_name)
    service.users().messages().modify(userId=GMAIL_USER_ID, id=msg_id, body={'addLabelIds': [label_id]}).execute()

def get_or_create_label(label_name):
    labels = service.users().labels().list(userId=GMAIL_USER_ID).execute().get('labels', [])
    for label in labels:
        if label['name'] == label_name:
            return label['id']
    new_label = {'name': label_name, 'labelListVisibility': 'labelShow', 'messageListVisibility': 'show'}
    created = service.users().labels().create(userId=GMAIL_USER_ID, body=new_label).execute()
    return created['id']
