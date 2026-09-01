import ollama
import httpx
from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST")

client = ollama.Client(
  host=OLLAMA_HOST,
  timeout=25.0,
)

while True:
  text = input("Enter text: ")
  
  if text == "":
    continue

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
          'Translate the user\'s text, regardless of the language, into natural English used today in the U.S. ' 
          'Preserve the original meaning and tone. ' 
          'If there are obvious typos or missing accents, silently correct them when interpreting the text. ' 
          f'Return only the translation, with absolutely nothing else: "{text}"'
        ),
      },
    ],
  think=False,
  stream=True,
)
    
    for chunk in response:
      print(chunk.message.content, end="", flush=True)
   
    print()
    
  except (httpx.ConnectTimeout, httpx.ReadTimeout):
    print("Error: Unable to connect to the Ollama server. Please check your connection and try again.")
    