import requests

def fetch_digimon_data():
    url = "https://digimon-api.vercel.app/api/digimon"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Ocorreu um erro ao fazer a requisição: {e}')
        return []

dados_digimon = fetch_digimon_data()

