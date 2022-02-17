### Criando função para verificar se duas strings são anagramas
def verifica_anagrama(palavra1, palavra2):
    cont = 0
    for x in palavra1:
        for y in palavra2:
            if x == y:
                cont += 1
                break
    if palavra1 == palavra2:
        return True
    if len(palavra1) != len(palavra2):
        return False
    elif cont == len(palavra1):
        return True
    else:
        return False

### função para separar todas as substrings
def cria_substring(palavra):
  lista_substring = list(palavra)
  cont = 1
  for x in range(len(palavra)):
    for y in range(len(palavra)):
      if palavra[x:cont] not in lista_substring:
        lista_substring.append(palavra[x:cont])
      
      cont +=1

  return lista_substring

### loop
while True:
  palavra = input('digite uma palavra: ')
  palavra = cria_substring(palavra)
  cont = 0
  cont_anagramas = 0
  anagramas = []
  ###comparando todas as substrings para saber se são anagramas
  for x in range(len(palavra)):
    cont = 0
    for y in range(len(palavra)):
      if verifica_anagrama(palavra[x],palavra[y]) == True:
        cont += 1   
        if palavra[x] and palavra[y] not in anagramas:
          anagramas.append(palavra[x] + palavra[y])
    if cont > 1:
      cont_anagramas += 1
  
  print("\nA palavra possui",int(cont_anagramas/2)," anagramas\n")
 
  exit = input("deseja encerrar? s//n\n ")
  if exit == "s":
    break
