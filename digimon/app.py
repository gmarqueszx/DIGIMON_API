from flask import Flask, render_template, request
from api_digimon import dados_digimon

app = Flask(__name__)

@app.route('/')
def index():
    print("Carregando a página inicial...")
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    nome_digimon_usuario = request.form['digimon_name'].capitalize()
    print(f"Procurando por: {nome_digimon_usuario}")
    for digimon in dados_digimon:
        if digimon['name'] == nome_digimon_usuario:
            print(f"Digimon encontrado: {digimon}")
            return render_template('index.html', digimon=digimon)
    print("Digimon não encontrado.")
    return render_template('index.html', error="Digimon não encontrado, tente novamente.")

if __name__ == "__main__":
    app.run(debug=True)