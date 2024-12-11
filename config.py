from dotenv import load_dotenv
import os

load_dotenv()

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key
