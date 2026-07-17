from google import genai

from config import api_key
from prompts import SYSTEM_PROMPT
from history import add_message, build_prompt

client = genai.Client(api_key=api_key)

print("=" * 50)
print("🤖 AI Placement Mentor")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Store user message
    add_message("user", user_input)

    # Build prompt using conversation history
    prompt = build_prompt(SYSTEM_PROMPT)

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_response = response.text

        print("\nMentor:", ai_response)

        # Store assistant response
        add_message("assistant", ai_response)

    except Exception as e:
        print("\nERROR:", e)



