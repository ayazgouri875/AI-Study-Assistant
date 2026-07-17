# utils.py

def validate_input(user_input: str):

    if user_input is None:
        return False, "Input cannot be None."

    user_input = user_input.strip()

    if user_input == "":
        return False, "Please enter a message."

    if len(user_input) > 1000:
        return False, "Message is too long. Maximum 1000 characters."

    return True, ""