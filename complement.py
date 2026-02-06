import requests
import json

url = "http://localhost:1234/v1/chat/completions"

with open("notes.txt", "r", encoding="utf-8") as file:
    notes = file.read()


prompt = f"""You are a specialized educational assistant. Analyze these class notes and:

1. Complement with relevant technical information
2. Add practical examples when possible
3. Explain concepts clearly
4. Suggest additional study resources

NOTES:
{notes}

DETAILED COMPLEMENT"""


data = {
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.7,
    "max_tokens": 2000
}

print("🔄 Processing...")
response = requests.post(url, json=data)
ai_content = response.json()['choices'][0]['message']['content']


with open("notes_complemented.txt", "w", encoding="utf-8") as file:
    file.write("=== ORIGINAL NOTES ===\n")
    file.write(notes)
    file.write("\n\n" + "="*50 + "\n")
    file.write("\n\n=== AI COMPLEMENT ===\n")
    file.write(ai_content)

print("Complemented file saved!")
