# history.py

history = []


def add_message(role, content):
    """
    Add a message to the conversation history.
    """

    history.append({
        "role": role,
        "content": content
    })


def build_prompt(system_prompt):
    """
    Convert conversation history into a prompt for Gemini.
    """

    prompt = system_prompt + "\n\nConversation:\n"

    for message in history:
        prompt += f"{message['role'].capitalize()}: {message['content']}\n"

    return prompt


def clear_history():
    """
    Clear all stored messages.
    """

    history.clear()