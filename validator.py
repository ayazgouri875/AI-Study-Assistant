from logger import logger


class Validator:

    def __init__(self, max_length=1000):
        self.max_length = max_length

    def validate(self, user_input: str):

        if user_input is None:
            logger.warning("Validation failed: Input is None.")
            return False, "Input cannot be None."

        user_input = user_input.strip()

        if user_input == "":
            logger.warning("Validation failed: Empty input.")
            return False, "Please enter a message."

        if len(user_input) > self.max_length:
            logger.warning("Validation failed: Input exceeds maximum length.")
            return False, f"Message exceeds {self.max_length} characters."

        return True, ""