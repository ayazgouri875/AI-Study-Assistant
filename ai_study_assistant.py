#    Main Controller
from config import api_key, model_name
from validator import Validator
from history import HistoryManager
from prompt_manager import PromptManager
from gemini_client import GeminiClient
from logger import logger


class AIStudyAssistant:

    def __init__(self):

        logger.info("Initializing AI Study Assistant...")

        self.validator = Validator()
        self.history = HistoryManager()
        self.prompt_manager = PromptManager()
        self.gemini = GeminiClient(api_key)

        self.current_role = "placement"

        logger.info("AI Study Assistant initialized successfully.")

    def process_request(self):

        # -----------------------------------
        # User Input
        # -----------------------------------
        user_input = input("\nYou: ")

        logger.info("User submitted a prompt.")

        if user_input.lower() == "exit":

            logger.info("Application closed.")
            print("Goodbye!")

            return False

        # -----------------------------------
        # Validate Input
        # -----------------------------------
        valid, error = self.validator.validate(user_input)

        if not valid:

            print(f"\n⚠ {error}")
            return True

        # -----------------------------------
        # Store User Message
        # -----------------------------------
        self.history.add_message("user", user_input)

        # -----------------------------------
        # Build Prompt
        # -----------------------------------
        system_prompt = self.prompt_manager.get_prompt(
            self.current_role
        )

        prompt = self.history.build_prompt(system_prompt)

        logger.info("Prompt built successfully.")

        # -----------------------------------
        # Generate Response
        # -----------------------------------
        response = self.gemini.generate_response(
            model_name,
            prompt
        )

        # -----------------------------------
        # Handle Response
        # -----------------------------------
        if response.success:

            logger.info("Successfully received response from Gemini API.")

            print(f"\nMentor: {response.text}")

            self.history.add_message(
                "assistant",
                response.text
            )

        else:

            logger.error(
                f"Response generation failed: {response.error}"
            )

            print(f"\nERROR: {response.error}")

        return True

    def run(self):

        print("=" * 50)
        print("🤖 AI Placement Mentor")
        print("Type 'exit' to quit")
        print("=" * 50)

        while True:

            if not self.process_request():
                break