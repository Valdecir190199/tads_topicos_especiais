# Este é um comentário

'''
Comentário em bloco
- Três áspas simples ou três áspas duplas

'''

print("Olá 3º ano do TADS!")

print("Maravilha rapah!")

nome = "Rafael"

# Concatenação com o +
print("Olá " + nome)

# Entrada de dados pelo terminal. Por padrão toda entrada é string
nome = input("Digite seu nome: ")
print(nome + " bem vindo ao sistema!")

# Quando trabalhamos com números, temos que converter a variável
idade = input("Digite sua idade: ")
idade = int(idade)
# idade = float(idade)

'''
Operadores

+
-
*
/

** é usado para calcular Potência. Por exemplo:
2**3 = 8
8**2 = 64

A raiz de um número é ele elevado a (1/x)
16**(1/2) - raiz quadrada de 16
16**(1/3) - raiz cúbica de 16
257**(1/5) - raiz de grau 5
'''

print("A raiz é", 16**(1/4) )

'''
Condicionais

and = e
or = ou

'''
a = 20

if a > 10:
    # Converte a variável para string
    print( str(a) + " é maior que 10.")

elif a < 10 :
    print( str(a) + " é menor do que 10.")

else:
    print( str(a) + " é igual a 10.")

'''
Laços de repetição WHILE
'''
x = 1
t = 8

while x <= 10:

    print(x, "x", t, "=", t*x)

    x += 1
# A identação define o final ou o que pertence a algum laço
print("Aqui o while já terminou!")
