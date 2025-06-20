# Josh AutoResponder AI

A Google Cloud Function that reads incoming Gmail messages, generates a professional reply using OpenAI, and replies in the same thread. Replies are logged to BigQuery, and duplicates are avoided with labels.

## Setup

1. Enable Gmail API and BigQuery API in Google Cloud Console.
2. Create a service account with Gmail and BigQuery access.
3. Create a BigQuery table: `your_project.your_dataset.email_responses`.
4. Set environment variable `OPENAI_API_KEY`.

## Deploy

```bash
gcloud functions deploy auto_reply_handler \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --env-vars-file .env.yaml
```

Use Cloud Scheduler to invoke periodically (every 5 mins).
