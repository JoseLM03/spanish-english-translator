import ollama
import httpx
from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST")

client = ollama.Client(
  host=OLLAMA_HOST,
  timeout=10.0,
)

while True:
  text = input("Enter text: ")
  
  if text == "exit":
    print("Goodbye!")
    break
  
  try:
    response = client.chat(
    model='qwen3.5:9b', 
    messages=[
      {
        'role': 'user',
        'content': (
          'Translate the user\'s text into natural English used today in the U.S. ' 
          'Preserve the original meaning and tone. ' 
          'If there are obvious typos or missing accents, silently correct them when interpreting the text. ' 
          f'Return only the translation, with absolutely nothing else: "{text}"'
        ),
      },
    ],
  think=False,
)
    print(response.message.content)
  except httpx.ConnectTimeout:
    print("Error: Unable to connect to the Ollama server. Please check your connection and try again.")