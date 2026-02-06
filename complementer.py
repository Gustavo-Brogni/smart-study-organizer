import requests
import json

# LMStudio Server URL
url = "http://localhost:1234/v1/chat/completions"


while True:

    files = []

    qntfiles = int(input("Enter how many files you wish to complement: "))
    for i in range(qntfiles):
            file = input(f"Enter the name of the {i + 1}º file: ")
            files.append(file)

    notes = ""

    try:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                   notes += f.read()
        break
    except FileNotFoundError:
            print(f"{file}: Wrong file name or path.")

       

MAX_CHARS = 8000
if len(notes) > MAX_CHARS:
    notes = notes[:MAX_CHARS]
    print(f"The content was condensed to {MAX_CHARS} to fit context")


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


with open("complemented_notes.txt", "w", encoding="utf-8") as file:
    file.write("=== ORIGINAL NOTES ===\n")
    file.write(notes)
    file.write("\n\n" + "="*50 + "\n")
    file.write("\n\n=== AI COMPLEMENT ===\n")
    file.write(ai_content)

print("✅ Complemented file saved!")

