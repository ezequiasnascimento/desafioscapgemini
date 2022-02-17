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

p = input()
cont_anagramas = 0
cont = 0
for i in range(len(p)):
   
    print(p.count(p[i::],i+1))
    if cont > 1:
        cont_anagramas += 1
print(cont_anagramas)
