# Salvar cada frase com seu autor em uma nova linha dentro de um arquivo chamado frases.txt

import requests
contador = 0
while contador <= 3:
    contador += 1
    resposta = requests.get('https://zenquotes.io/api/random')
    dados = resposta.json()
    with open('frases.txt', 'a') as file:
        frase = dados[0]["q"]
        autor = dados[0]["a"]
        file.write(f'"{frase}" - {autor}\n')
        print(frase)