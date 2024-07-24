from api_digimon import dados_digimon
import time


print('DigimonDex\n')

print('1. Procurar Digimon')
print('2. Sair\n')

while True:
    opcao_escolhida = input('Escolha a opção desejada: ')
    if opcao_escolhida == '1':
        nome_digimon_usuario = input("Digite o nome do Digimon: ")
        
        if nome_digimon_usuario in dados_digimon:
                digimon = dados_digimon[nome_digimon_usuario]
                print(f"Nome: {nome_digimon_usuario}")
                print(f"Nível: {digimon['level']}")
        else:
                print("Digimon não encontrado, tente novamente.")
                time.sleep(3)
    else:
        print('Finalizando programa...')
        time.sleep(3)
        break
