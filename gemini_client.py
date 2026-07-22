from google import genai

from logger import logger

from ai_response import AIResponse

class GeminiClient:

    def __init__(self, api_key):

        self.client = genai.Client(api_key=api_key)

        logger.info("Gemini Client initialized successfully.")

    def generate_response(self, model, prompt):

        try:

            response = self.client.models.generate_content(
                model=model,
                contents=prompt
            )

            if not response.text:

                logger.warning("No response received from Gemini.")

                return False, None, "No response received."

            logger.info("Response generated successfully.")

            return AIResponse(
             success=True,
             text=response.text
             )

        except Exception as e:

            logger.error(f"Gemini API Error: {e}")

            return AIResponse(
            success=False,
            error=str(e)
            )