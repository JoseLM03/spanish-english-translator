import ollama

client = ollama.Client(
  host='http://192.168.64.1:11434',
)

response = client.chat(
  model='qwen3.5:9b', 
  messages=[
    {
      'role': 'user',
    'content': 'Hola, como estas?',
    },
  ],
  think=False,
)

print(response.message.content)