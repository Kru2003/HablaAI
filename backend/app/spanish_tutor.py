import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Create Gemini client
client = genai.Client()

# 2. Define the Spanish teacher's personality
SYSTEM_INSTRUCTION = """
You are HablaAI, a friendly Spanish language teacher.

STUDENT PROFILE:
- Native language: English
- Spanish level: Beginner (A1)
- Learning goal: Speaking, listening, reading and writing

TEACHING RULES:
1. Use simple Spanish.
2. Explain difficult concepts in English.
3. Correct grammar mistakes gently.
4. Give the corrected Spanish sentence.
5. Explain why the correction is needed.
6. Teach useful everyday vocabulary.
7. Ask only one question at a time.
8. Encourage the student to speak Spanish.
"""

# Store active conversations in memory
conversations = {}

# 3. Create a chat session
def create_chat():
    """Create a new Gemini conversation."""
    return client.chats.create(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7,
        ),
    )


def get_tutor_response(message: str, conversation_id: str | None = None):
    """Send a message to Gemini and return its response."""

    # Reuse an existing conversation, or create a new one
    if conversation_id and conversation_id in conversations:
        chat = conversations[conversation_id]
    else:
        chat = create_chat()

        # Use the supplied ID for an existing-but-unknown ID,
        # otherwise generate a new ID.
        import uuid

        conversation_id = conversation_id or str(uuid.uuid4())
        conversations[conversation_id] = chat

    response = chat.send_message(message)

    return {
        "conversation_id": conversation_id,
        "reply": response.text,
    }
