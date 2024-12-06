def show(alvo, letras_usadas) :
  for letra in alvo :
    if letra in letras_usadas :
      print(letra, end = " ")
    else :
      print("_", end = " ")
  print()
  print()


perdeu = False

while not perdeu :

  alvo = "BOLA"
  erros = 0
  acertos = 0
  acertou = False
  usadas = []

  while not acertou and erros < 6 :

    print("Você tem", 6 - erros, "tentativas: ", end=" ")
    show(alvo,usadas)
    letra = input("Digite uma letra: ").upper()

    if letra in usadas :
      print("Letra repetida!")
    else :
  
      usadas.append(letra)

      if letra in alvo :
        print("\nA letra existe\n")
        acertos = acertos + 1
        if acertos == len(alvo) :
          acertou = True
      else :
        erros = erros + 1
        print("\nA letra não existe!\n")
  
  if acertou :
    print("Parabéns! Você acertou a palavra", alvo)
  else :
    print("Você perdeu, a palavra era", alvo)
    perdeu = True



print("GAME OVER!")

