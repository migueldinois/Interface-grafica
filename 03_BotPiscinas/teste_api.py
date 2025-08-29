from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyAqHTr0DulKHBhwpSIeIEZv4QSo0lfiHX8")

pergunta = input("Pergunte algo a i.a: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="Você é um especialista em piscinas, com mais de 1005 anos no mercado, você entende tudo, é o melhor de todos, o mais reconhecido em toda a historia"),
    contents=f"{pergunta}"
)

print(response.text)