from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyAqHTr0DulKHBhwpSIeIEZv4QSo0lfiHX8")
chat = client.chats.create(model="gemini-2.5-flash")

pergunta = input("Pergunte algo a i.a: ")

response = chat.send_message_stream(pergunta)
for chunk in response:
    print(chunk.text, end="")

