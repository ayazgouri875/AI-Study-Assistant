import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("Gemini_API_Key")
model_name = os.getenv("MODEL_NAME")