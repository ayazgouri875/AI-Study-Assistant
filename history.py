# history_manager.py

class HistoryManager:
    """
    Manages conversation history for a single chat session.
    """

    def __init__(self):
        # Each object gets its own history
        self.history = []

    def add_message(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def build_prompt(self, system_prompt):
        prompt = system_prompt + "\n\nConversation:\n"

        for message in self.history:
            prompt += f"{message['role'].capitalize()}: {message['content']}\n"

        return prompt

    def clear(self):
        self.history.clear()

    def get_history(self):
        return self.history