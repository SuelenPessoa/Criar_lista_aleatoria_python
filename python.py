import random as r

lista = [] #Cria uma lista vazia
i = 1  # da o valor para o i.

while i <= 20:   # Enquanto ... i que é 1 for menor ou igual a 20..
    lista.append(r.randrange(1,100, 2)) #acrescenta "append" um numero aleatório com "randrange" na lista entre 1, e 100.
    i = i+1  #acrescenta + 1  até preencher a lista até 20.

    print(f'Essa foi a lista gerada aleatóriamente: {lista}') #printa na tela dessa forma, trazendo a variavel.


def maior_valor(lista):
    return max(lista, key=int) #trás o máximo da lista, do tipo inteiro.
m = maior_valor(lista)

print (f'Maior valor é : {m}') 