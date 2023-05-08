
import sys

idade = int(input("Qual a sua idade: \n"))

idade1 = 18
if idade < idade1:
    print("Voce é menor de idade \n ")
    sys.exit()
else:
    print("Voce é maior de idade \n")


p = float(input("Digite um número: "))
s = float(input("Digite um número: "))

print(""" Observe os tipos de operações póssíveis:
                (1) Soma \n
                (2) Subtração \n
                (3) Divisão \n
                (4) Multiplicação \n """)

calculo = int(input("Digite a opção que você deseja executar: "))

match calculo:
    case 1:
        soma = (p + s)
        print("A soma entre %d e %d é igual à: %d \n" % (p, s, soma))

    case 2:
        sub = (p - s)
        print("A subtração entre %d e %d é igual à: %d \n" % (p, s, sub))

    case 3:
        div = (p / s)
        print("A divisão entre %d e %d é igual à: %d \n" % (p, s, div))

    case 4:
        mult = (p * s)
        print("A multiplicação entre %d e %d é igual à: %d \n" % (p, s, mult))

    case _:
        print("Opção inválida")



#Classificar se a letra é vogal ou consoante - Exercício #4

letra = input("Informe uma letra: ")
match letra:
    case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U" :
        print("Vogal")
    case _:
        print("Consoante")

#QUESTAO 1 - Crie um algoritmo que exibe os números inteiros de 1 a 1000.
for i in range(1,1001):
    print(i)

#QUESTAO 2 - Escreva um algoritmo que solicite 5 números e exiba o quadruplo de cada número digitado.
for i in range(5):
    num = float(input("Digite um número: "))
    quadruplo = num * 4
    print("O quadruplo:" , num, "é",quadruplo)

#QUESTAO 3 - Escreva um algoritmo que solicite a idade de 20 pessoas e informe a quantidade de
# pessoas que não podem entrar em um pub (idade inferior a 18 anos)

for i in range(20):
    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        print("Voce pode entrar! \n")
    else:
        print("Voce nao pode entrar! \n")

#QUESTAO 4 - Escreva um algoritmo que solicite 10 números e informe quantos
# números entre 1 e 1000 foram digitados.

b = 0
for i in range(10):
    num = float(input("Digite um número: "))
    if num >= 1 and num <= 1000:
        b +=1

print("Foram digitados" ,b, "numeros entre 1 e 1000." )



#QUESTAO 5- Escreva um algoritmo que solicite 10 números e informe o somatório de
# todos os números pares que foram digitados.

soma = 0

for i in range(10):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        soma += num

print("A soma dos números pares é:", soma)

#QUESTAO 6- Solicite vários números ao usuário (até que ele digite zero) e e na
# sequencia informe a média dos números digitados.

soma1 = 0
contador = 0

while True:
    num = float(input("Digite um número (digite 0 para sair): "))
    if num == 0:
        break

    soma1 += num
    contador += 1

if contador > 0:
    media = soma1 / contador
    print("A média dos números digitados é: {:.2f}".format(media))
else:
    print("Nenhum número foi digitado.")

# QUESTAO 7 - Solicite dois números diferentes ao usuário. Se os números forem iguais,
# solicite novamente) e informe a diferença entre o maior e o menor número.

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 == num2:
        print("Os números devem ser diferentes. Tente novamente.")
    else:
        break

maior = max(num1, num2)
menor = min(num1, num2)
diferenca = maior - menor

print("A diferença entre o maior e o menor número é:", diferenca)


# QUESTAO 8 - Escreva um algoritmo que solicite 20 números e informe qual foi o menor
# número digitado.

numeros = []

for i in range(20):
    num = float(input("Digite um número: "))
    numeros.append(num)

menor = min(numeros)

print("O menor número digitado foi:", menor)


#QUESTAO - 9 Faça um algoritmo que solicite N números e calcule a soma para os
# números pares e para os impares ímpares

n = int(input("Quantos números você deseja digitar? "))
numeros = []

for i in range(n):
    num = int(input("Digite um número: "))
    numeros.append(num)

soma_pares = 0
soma_impares = 0

for num in numeros:
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print("A soma dos números pares é:", soma_pares)
print("A soma dos números ímpares é:", soma_impares)

#QUESTAO 10- Faça um algoritmo que solicite N números e calcule a média para os
# números pares e para os impares ímpares

n = int(input("Digite a quantidade de números: "))

soma_pares = 0
qtd_pares = 0
soma_impares = 0
qtd_impares = 0

for i in range(n):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma_pares += num
        qtd_pares += 1
    else:
        soma_impares += num
        qtd_impares += 1

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"A média dos números pares é {media_pares:.2f}")
else:
    print("Não foram digitados números pares")

if qtd_impares > 0:
    media_impares = soma_impares / qtd_impares
    print(f"A média dos números ímpares é {media_impares:.2f}")
else:
    print("Não foram digitados números ímpares")

#QUESTAO 11- Crie um algoritmo para calcular o fatorial de um numero digitado. O
# fatorial é uma multiplicação do numero N por seus antecessores até 1
# n! = n x (n-1) x (n-2) x ... x 3 x 2 x 1

i = 1
num = int(input("Digite um número: "))
res = num

while i < num:
    res *= i
    i += 1
    print(res)
    
#QUESTÃO 12- Crie um algoritmo que resolva o valor de S para a série:
#1 + 1/1 + 1/2 + 1/3 + 1/4 ... 1/N

i = 1
num1 = int(input("Digite um número: "))
res1 = 1

while i < num1:
    res1 += 1/i
    i += 1
    print(res1)
    
  
#QUESTÃO 13- 

n = int(input("Digite um número inteiro e positivo: "))
if n <= 1:
    print(n , "não é primo")
else: 
    primos = []
    for i in range(2, n+1):
        primo= True
        for j in range (2,i):
            if i % j == 0:
                primo = False
                break
        if primo:
            primos.append(i)
                
    print("Números primos até", n, ":")
    print(primos)
    print("Total de números primos: " , len(primos))
