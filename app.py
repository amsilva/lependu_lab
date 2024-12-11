import requests
import csv


def nova_palavra():

  #endpoint = "https://faccamp.pythonanywhere.com/hangman-api/getword"
  endpoint = "https://faccamp.pythonanywhere.com/hangman-api/getdata"

  try:
    resposta = requests.get(endpoint)
    dado = resposta.json()  # desserializar para JSON
    return dado             # layout.json {palavra:"PALAVRA"}

  except requests.exceptions.RequestException as e:
    print("Erro na conexão com api:", e)



def show(alvo, letras_usadas) :
  for letra in alvo :
    if letra in letras_usadas :
      print(letra, end = " ")
    else :
      print("_", end = " ")

  print()



global nome_arquivo
nome_arquivo = 'rec5.csv'

# recupera dados do arquivo em json
def ler_arquivo():
    dados = []

    try :
      with open(nome_arquivo, mode='r') as file:
        buffer = csv.reader(file)
        for linha in buffer:
            id = linha[0]
            pontos = int(linha[1])
            dados.append({'id': id, 'pontos': pontos})
    except FileNotFoundError:
      return []

    return dados

# salvar o arquivo de recordes
def salvar_arquivo(dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        escritor = csv.writer(file)
        for item in dados:
            escritor.writerow([item['id'], item['pontos']])



## main

perdeu = False
fase = 0
pontos_total = 0

while not perdeu :


  fase = fase + 1 
  combo = 0
  mcombo = 0
  erros = 0
  acertos = 0
  acertou = False
  usadas = []
  #alvo = "GOIABA"
  dadojson = nova_palavra()
  #print(dadojson)
  #alvo = 'POP'
  alvo = dadojson["palavra"]
  dica2 = dadojson["categoria"]
  #complexidade = dadojson["complexidade"]  

  S = len(alvo) #Size da palavra alvo
  D = 1 #(complexidade) dificuldade da palavra alvo
  N = len(set(alvo)) #diff de letras do alvo
  #E #quantidade de erros
  #C #combo de acertos consecutivos  

  print(f"\nFASE: {fase} [", end='')
  barra = '*' * fase
  print(f"{barra}]")

  while not acertou and erros < 6 :

    print("Você tem", 6 - erros, "tentativas: ", end=" ")

    if erros > 2 : 
           print(f"({dica2})", end=" ")

    show(alvo,usadas)
    letra = input("Digite uma letra: ").upper()

    if letra in usadas :
        print("\nLetra repetida!")
    else :
  
        usadas.append(letra)

        if letra in alvo :
            combo += 1
            print("\nLetra existente\n")
            acertos = acertos + alvo.count(letra)
            print(acertos)
            if acertos == len(alvo) :
                acertou = True
        else :
            combo = 0
            erros = erros + 1
            print("\nErro! Letra não existente!\n")

        if combo > mcombo : 
            mcombo = combo
  
  if acertou :
    E = 6 - erros #assertividade
    C = mcombo
    pontos_acerto = (S + D) * (N +E) + C
    pontos_total += pontos_acerto
    print("Parabéns! Você acertou a palavra", alvo, "com", pontos_acerto, "pontos!")
  else :
    print("Você perdeu, a palavra era", alvo)
    print("Pontuação total =", pontos_total)
    perdeu = True

print("GAME OVER!")

# manipulando os recordes
recordes = ler_arquivo()

ultimo = recordes[4] #ultima posicao do top-5
#print("ultimo = ", ultimo)
#rint("ultimo ponto = ", ultimo['pontos'])

if pontos_total > ultimo['pontos'] :

    print("\n** Parabéns! Sua pontuação entra no Top-5 List")
    ident = input("SUA IDENTIFICAÇÃO: ").upper()
    novo = {"id":ident, "pontos":pontos_total}
    recordes.append(novo)
    recordes = sorted(recordes, key=lambda filtro: filtro["pontos"], reverse=True)
    recordes.pop()

salvar_arquivo(recordes)

print("\n*** Recordes Top-5 ***")

for item in recordes :
    print(f"{item['id']} - {item['pontos']}")
