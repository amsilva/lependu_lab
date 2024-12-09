import requests


def nova_palavra():

  endpoint = "https://faccamp.pythonanywhere.com/hangman-api/getword"

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
  alvo = "GOIABA"
  S = len(alvo) #Size da palavra alvo
  D = 1 #dificuldade da palavra alvo
  N = len(set(alvo)) #diff de letras do alvo
  #E #quantidade de erros
  #C #combo de acertos consecutivos  

  print("\n*** FASE:", fase)

  while not acertou and erros < 6 :

    print("Você tem", 6 - erros, "tentativas: ", end=" ")
    show(alvo,usadas)
    letra = input("Digite uma letra: ").upper()

    if letra in usadas :
        print("Letra repetida!")
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
    print("* combo = ", mcombo)
    C = mcombo
    pontos_acerto = (S + D) * (N +E) + C
    pontos_total += pontos_acerto
    print("Parabéns! Você acertou a palavra", alvo, "com", pontos_acerto, "pontos!")
  else :
    print("Você perdeu, a palavra era", alvo)
    print("Pontuação total =", pontos_total)
    perdeu = True



print("GAME OVER!")

