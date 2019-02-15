# Trabalhando com uma lista no tamanho 10
# Ou seja, um vetor vazio com 10 posições
list = [""]*10

# Trabalando com listas sem identificar tamanho
lista = []

# Adicionar um elemento na lista

lista.append(5)
lista.append(4)
lista.append(2)
lista.append(8)
lista.append(2)

# Manipulando valores da lista
lista[0] = 2

# Obtendo o tamanho da lista
t = len(lista)

# Exibindo uma lista
print("Resultado da lista: ", lista)

i = 0
while i < t:
    print("Na posição", i, "tem o valor", lista[i])
    i+=1

while i < t:
    print("Na posição {} tem o valor {}".format(i, lista[i]))
    i+=1

print("-----------------------")

# Usando for na maneira foreach
for x in lista:
    print("Valor da lista ", x)

# uso do for normal
# len calcula o tmanho da lista  range cria uma sequenca numerica
for i in range( len(lista) ):
    print ("Na posição {} tem o valor {}.".format(i, lista[i]))

#criando funções em python

def dobro(num):
    d = num * 2
    print("o dobre de {} e {}.".format(num, d))
