# Josh AutoResponder Gemini

A Google Cloud Function that reads Gmail messages, uses Gemini to generate professional replies, and responds in the same thread. Replies are logged to BigQuery and duplicates are avoided using labels.

## Setup

1. Enable Gmail API, BigQuery, and Vertex AI in Google Cloud Console.
2. Create a service account with access to Gmail, BigQuery, and Vertex AI.
3. Create a BigQuery table: `your_project.your_dataset.email_responses`.
4. Deploy the Cloud Function with Vertex AI support.

## Deploy

```bash
gcloud functions deploy auto_reply_handler \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --env-vars-file .env.yaml
```

Use Cloud Scheduler to invoke periodically (e.g., every 5 mins).
