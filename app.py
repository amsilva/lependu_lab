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
  erros = 0
  acertos = 0
  acertou = False
  usadas = []
  alvo = "BALA"
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
        print("\nLetra existente\n")
        acertos = acertos + alvo.count(letra)
        print(acertos)
        if acertos == len(alvo) :
          acertou = True
      else :
        erros = erros + 1
        print("\nErro! Letra não existente!\n")
  
  if acertou :
    E = 6 - erros #assertividade
    pontos_acerto = (S + D) * (N +E)
    pontos_total += pontos_acerto
    print("Parabéns! Você acertou a palavra", alvo, "com", pontos_acerto, "pontos!")
  else :
    print("Você perdeu, a palavra era", alvo)
    print("Pontuação total =", pontos_total)
    perdeu = True



print("GAME OVER!")

