import requests
import json 

url = 'https://digimon-api.vercel.app/api/digimon'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_digimon = {}
    for item in  dados_json:
        nome_digimon = item['name']
        if nome_digimon not in dados_digimon:
            dados_digimon[nome_digimon] = []

            dados_digimon[nome_digimon].append({
                "img": item['img'],
                "level": item['level'],
            })
else:
    print(f'Ocorreu um erro na requisisão, erro: {response.status_code}')

for nome_digimon, dados in dados_digimon.items():
    nome_do_arquivo = f'{nome_digimon}.json'
    with open(nome_do_arquivo,'w') as arquivo_digimon:
        json.dump(dados,arquivo_digimon,indent=4)