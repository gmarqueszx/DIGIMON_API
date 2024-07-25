

DigimonDex:
Este é um projeto simples de um aplicativo web que permite aos usuários procurar informações sobre Digimons, como imagens e nível, usando a API Digimon.

Estrutura do Projeto:
digimon_app/
├── api_digimon.py
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── favicon.ico
    └── styles.css

Pré-requisitos:
Python 3.x
Flask
Requests

Instalação:

Clone este repositório:
git clone https://github.com/seu_usuario/digimondex.git

Navegue até o diretório do projeto:
cd digimondex

Crie um ambiente virtual:
python -m venv venv

Ative o ambiente virtual:
No Windows:
venv\Scripts\activate

No Linux/Mac:
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Executando o Projeto:
Inicie o servidor Flask:
python app.py

Abra o navegador e acesse:

http://127.0.0.1:5000

Estrutura dos Arquivos:
api_digimon.py
Este arquivo contém a lógica para fazer a requisição à API Digimon e armazenar os dados em um dicionário.

app.py
Este arquivo contém a lógica do servidor Flask, incluindo as rotas para a página inicial e a funcionalidade de busca de Digimons.

templates/index.html
Este arquivo é o template HTML para a interface do usuário. Ele contém um formulário para buscar Digimons e exibe os resultados.

static/favicon.ico
Este é o favicon para o aplicativo.

static/styles.css
Este arquivo contém os estilos CSS para a interface do usuário.

Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Faça um fork do projeto.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça suas modificações.
Faça um commit das suas mudanças (git commit -am 'Adiciona nova funcionalidade').
Faça um push para a branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request.
