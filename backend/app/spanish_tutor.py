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

Start by introducing yourself in Spanish.
"""

# 3. Create a chat session
chat = client.chats.create(
    model="gemini-3.1-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.7,
    ),
)

print("===================================")
print("       Welcome to HablaAI")
print("===================================")
print("Your personal Spanish tutor")
print("Type 'exit' to quit.")
print()

# 4. Interactive conversation loop
while True:

    user_message = input("You: ")

    if user_message.lower() in ["exit", "quit"]:
        print("HablaAI: ¡Hasta luego!")
        break

    # 5. Send message to Gemini
    response = chat.send_message(user_message)

    # 6. Display AI response
    print("\nHablaAI:", response.text)
    print()
