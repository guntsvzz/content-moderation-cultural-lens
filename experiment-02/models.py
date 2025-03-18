from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Step 1: Load environment variables from .env file
load_dotenv(".env")

# Step 2: Retrieve Azure OpenAI environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
DEPLOYMENT_NAME = "gpt-4o-mini"  # e.g., "gpt-35-turbo" or "gpt-4"

# Step 3: Initialize Azure OpenAI client
client = AzureOpenAI(
    api_version=OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def get_chat_response(prompt) -> str:
    completion = client.chat.completions.create(
        model=DEPLOYMENT_NAME, 
        messages=[{"role": "user", "content": prompt}],
    )

    return completion.choices[0].message.content

def get_chat_response_parser(prompt, response_format) -> str:
    parser = client.beta.chat.completions.parse(
        model=DEPLOYMENT_NAME, 
        messages=[{"role": "user", "content": prompt}],
        response_format = response_format
    )

    return parser.choices[0].message.parsed