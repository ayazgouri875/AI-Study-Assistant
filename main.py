from google import genai
from config import api_key

SYSTEM_PROMPT = """
You are a senior placement mentor with 10+ years of experience.

Rules:
- Explain concepts simply.
- Give interview examples.
- Help students preparing for Data Science placements.
- If the user makes a mistake, guide instead of directly giving the answer.
"""

history = []

print("=" * 50)
print("🤖 AI Placement Mentor")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    history.append(f"User: {user_input}")

    prompt = SYSTEM_PROMPT + "\n\n" + "\n".join(history)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_response = response.text
        print("\nMentor:", ai_response)
        history.append(f"Assistant: {ai_response}")

    except Exception as e:
        print("\nERROR",e)




