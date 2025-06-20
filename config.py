import os

GMAIL_USER_ID = 'me'
LABEL_NAME = 'AutoReplied'

IGNORE_KEYWORDS = ['no-reply', 'noreply', 'auto-reply']
IGNORE_SENDERS = ['notifications@', 'do-not-reply@']

def should_ignore(subject, sender):
    if any(k in subject.lower() for k in IGNORE_KEYWORDS):
        return True
    if any(sender.lower().startswith(s) for s in IGNORE_SENDERS):
        return True
    return False
