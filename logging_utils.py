from google.cloud import bigquery
from datetime import datetime

client = bigquery.Client()

def log_to_bigquery(sender, subject, thread_id, message_id, response_text):
    table_id = "your_project.your_dataset.email_responses"
    row = [{
        'sender': sender,
        'subject': subject,
        'thread_id': thread_id,
        'message_id': message_id,
        'response': response_text,
        'timestamp': datetime.utcnow()
    }]
    client.insert_rows_json(table_id, row)
