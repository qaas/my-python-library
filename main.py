from dotenv import load_dotenv
from chat import chat_openai


load_dotenv()

response = chat_openai("gpt-4o", "How do I output all files in a directory using Python?")

print(response)

