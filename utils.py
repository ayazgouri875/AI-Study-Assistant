# utils.py

def validate_input(user_input: str):
    """
    Validate user input before sending it to Gemini.
    """

    if user_input is None:
        return False, "Input cannot be None."

    user_input = user_input.strip()

    if user_input == "":
        return False, "Please enter a message."

    if len(user_input) > 1000:
        return False, "Message is too long (Maximum 1000 characters)."

    return True, ""


def safe_generate_response(client, model: str, prompt: str):
    """
    Generate a response safely from Gemini.

    Returns:
        success (bool)
        response (str | None)
        error (str | None)
    """

    try:

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        if not response.text:
            return False, None, "No response received from Gemini."

        return True, response.text, None

    except Exception as e:
        return False, None, str(e)