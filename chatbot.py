import os

from dotenv import load_dotenv
from google import genai              
from google.genai import types


# Load environment variables from .env
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found! "
        "Please check your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=api_key)


# Create chat session
chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a highly capable, professional and friendly "
            "technical assistant. Keep answers clear and concise."
        )
    )
)


# Display assistant information
print("=" * 60)
print("Gemini AI Assistant Initiated")
print("Type 'quit', 'exit', or 'bye' to terminate the session")
print("=" * 60)


# Start conversation
while True:

    try:
        user_input = input("\nYou: ").strip()

        # Exit commands
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nAssistant: Session Terminated")
            break

        # Empty input
        if not user_input:
            print(
                "Assistant: Invalid input detected. "
                "Please enter a valid prompt."
            )
            continue

        # Send message to Gemini
        response = chat.send_message(
            message=user_input
        )

        # Display response
        print(f"\nAssistant: {response.text}")

    except Exception as e:
        print(f"\nSystem Error encountered: {e}")
        print(
            "Assistant: Failed to reach the API. "
            "Please verify your network connection, "
            "API key, and Gemini API configuration."
        )
        