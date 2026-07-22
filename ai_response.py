#  Response Object
class AIResponse:

    def __init__(self, success, text=None, error=None):

        self.success = success
        self.text = text
        self.error = error