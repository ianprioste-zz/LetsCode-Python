# Estrutura Condicionais

# 1.Faça um programa que peça a idade do usuário e imprima se ele é maior ou menor de 18 anos. 

idade = int (input("Digite a sua idade:"))

if idade >= 18:
    print("Você é maior de 18 anos")
else:
    print("Você é menor de 18 anos")

# 2. Faça um programa que peça um número e mostre se ele é positivo ou negativo. 

num = int (input("Digite um número:"))

if num >= 0:
    print("O número é positivo")
else:
    print("O número é negativo")

# 3.Faça um programa que dado um número digitado, mostre se ele é Par ou Ímpar.

num = int (input("Digite um número:"))

if num%2==0:
    print("O número é par")
else:
    print("O número é impar")

# 4.Faça um programa que peça dois números e mostre o maior deles. 

num1 = int (input("Digite um número:"))
num2 = int (input("Digite outro número:"))

if num1>=num2:
    print(num1,"é o maior número")
else:
    print(num2, "é maior número")

