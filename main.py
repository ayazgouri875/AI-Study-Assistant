from google import genai

from config import api_key
from prompts import SYSTEM_PROMPT
from history import add_message, build_prompt
from utils import validate_input, safe_generate_response

# Create Gemini client
client = genai.Client(api_key=api_key)

print("=" * 50)
print("🤖 AI Placement Mentor")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    # -----------------------------
    # Take User Input
    # -----------------------------
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # -----------------------------
    # Validate Input
    # -----------------------------
    valid, error = validate_input(user_input)

    if not valid:
        print(f"\n⚠ {error}")
        continue

    # -----------------------------
    # Store User Message
    # -----------------------------
    add_message("user", user_input)

    # -----------------------------
    # Build Prompt
    # -----------------------------
    prompt = build_prompt(SYSTEM_PROMPT)

    # -----------------------------
    # Generate Response
    # -----------------------------
    success, ai_response, error = safe_generate_response(
        client,
        "gemini-2.5-flash",
        prompt
    )

    # -----------------------------
    # Handle Response
    # -----------------------------
    if success:

        print(f"\nMentor: {ai_response}")

        add_message("assistant", ai_response)

    else:

        print(f"\nERROR: {error}")