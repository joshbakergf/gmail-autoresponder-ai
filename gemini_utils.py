from vertexai.preview.generative_models import GenerativeModel
import vertexai

def generate_response_with_gemini(prompt):
    vertexai.init(project="your-gcp-project", location="us-central1")
    model = GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
