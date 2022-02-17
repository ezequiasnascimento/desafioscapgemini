while True:  
  while True:
    while True:
      try:
        tamanho_escada = int(input("Escreva a quantidade de degraus da escada: "))
        break
      except ValueError:
        print("Por favor digite um número inteiro positivo\n")
        
    if tamanho_escada < 0:
      print("Por favor digite um número inteiro positivo\n")
      
      entrada = False
    elif tamanho_escada == 0:
      print("Entrada nula, por favor digitar novamente\n")
    else:
      break

  cont = tamanho_escada - 1

  for i in range(tamanho_escada):
      degrau = ''
      for y in range(tamanho_escada):
        if y >= cont:
          degrau = degrau + "*"
        else:
          degrau = degrau + " "
      cont = cont - 1
      print(degrau)
  resposta = input(("Deseja encerrar a aplicação? s//n "))
  if resposta == "s":
    break
  

