import requests
import json

url = "http://localhost:1234/v1/chat/completions"

with open("anotacoes.txt", "r", encoding="utf-8") as arquivo:
    anotacoes = arquivo.read()


prompt = f"""Você é um assistente educacional especializado. Analise estas anotações de aula e:

1. Complemente com informações técnicas relevantes
2. Adicione exemplos práticos quando possível
3. Explique conceitos de forma clara
4. Sugira recursos adicionais de estudo

ANOTAÇÕES:
{anotacoes}

COMPLEMENTO DETALHADO"""


dados = {
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.7,
    "max_tokens": 2000
}

print("🔄️ Processando...")
resposta = requests.post(url, json=dados)
conteudo_ia = resposta.json()['choices'][0]['message']['content']


with open("anotacoes_complementadas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=== ANOTAÇÕES ORIGINAIS ===\n")
    arquivo.write(anotacoes)
    arquivo.write("\n\n" + "="*50 + "\n")
    arquivo.write("\n\n=== COMPLEMENTO DA IA ===\n")
    arquivo.write(conteudo_ia)

print("Arquivo complementado salvo!")