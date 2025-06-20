from gmail_utils import get_unread_messages, get_message_content, send_email_reply_in_thread, apply_label
from openai_utils import generate_response
from logging_utils import log_to_bigquery
from config import GMAIL_USER_ID, LABEL_NAME, should_ignore

def auto_reply_handler(request=None):
    messages = get_unread_messages()
    for msg in messages:
        msg_id = msg['id']
        subject, sender, snippet, thread_id, message_id = get_message_content(msg_id)

        if should_ignore(subject, sender):
            continue

        prompt = f"""You received the following email:\nSubject: {subject}\nFrom: {sender}\nMessage: {snippet}\n\nReply professionally:"""
        reply_text = generate_response(prompt)
        send_email_reply_in_thread(sender, subject, reply_text, thread_id, message_id)
        apply_label(msg_id, LABEL_NAME)
        log_to_bigquery(sender, subject, thread_id, message_id, reply_text)

    return 'Processed'
