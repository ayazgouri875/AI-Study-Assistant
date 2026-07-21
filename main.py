from google import genai

from config import api_key, model_name
from prompts import SYSTEM_PROMPT
from history_manager import HistoryManager
from validator import Validator
from utils import safe_generate_response
from logger import logger

# -----------------------------------
# Initialize Objects
# -----------------------------------
logger.info("========== Application Started ==========")

client = genai.Client(api_key=api_key)

history = HistoryManager()
validator = Validator()

print("=" * 50)
print("🤖 AI Placement Mentor")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    # -----------------------------------
    # User Input
    # -----------------------------------
    user_input = input("\nYou: ")

    logger.info("User submitted a prompt.")

    if user_input.lower() == "exit":
        logger.info("Application closed.")
        print("Goodbye!")
        break

    # -----------------------------------
    # Validate Input
    # -----------------------------------
    valid, error = validator.validate(user_input)

    if not valid:
        print(f"\n⚠ {error}")
        continue

    # -----------------------------------
    # Store User Message
    # -----------------------------------
    history.add_message("user", user_input)

    # -----------------------------------
    # Build Prompt
    # -----------------------------------
    prompt = history.build_prompt(SYSTEM_PROMPT)

    logger.info("Prompt built successfully.")

    # -----------------------------------
    # Generate Response
    # -----------------------------------
    success, ai_response, error = safe_generate_response(
        client,
        model_name,
        prompt
    )

    # -----------------------------------
    # Handle Response
    # -----------------------------------
    if success:

        logger.info("Successfully received response from Gemini API.")

        print(f"\nMentor: {ai_response}")

        history.add_message("assistant", ai_response)

    else:

        logger.error(f"Response generation failed: {error}")

        print(f"\nERROR: {error}")
   