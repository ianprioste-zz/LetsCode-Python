# Estrutura de Sistemas
#   1º Entrada
#   2º Processamento
#   3º Saída

#Editores de texto
# Geral
# Python (Idle)
# Visua Studio Code

#Dados
# jupyter (linha a linha) jupyter.org
# Google colab



#SAÍDA

#print ("Olá, mundo")

#VARIÁVEIS

#Inteiros
#x = 10
#print(x)

# Reais (float)
#y = 3.2
#print(y)

#Texto (str)
#nome = "Ian"
#print(nome)

#Booleano (bool)
#a = True
#b = False

#print (a)

#x = 10
#print(x)
#x = "Oi"
#print (x)

#OPERAÇÕES MATEMÁTICAS

#x = 5
#y = 3

# Soma (+)
#print(x+y)

# Subtração (-)
#print (x-y)

# Multiplicação
#print (x*y)

# Divisão (/)
#print (x/y)

# Divisão Inteira (//)
#print (x//y)

# Resto da Divisão Inteira (%)
#print (x%y)

# Potenciação (**)
#print (x**y)


#ENTRADA

#idade = input("Digite a sua idade: ")
#print("A sua idade é", idade)

#a = int(input ("Digite um número: "))
#b = int(input ("Digite outro número: "))

#ESTRUTURAS CONDICIONAIS

# Menor (<)
print (3<5)

# Menor ou igual (<=)
print (3<=5)

# Maior (>)
print (3<5)

# Igual (==)
print (3==5)

# Diferente (!=)
print (3!=5)

# E (and)
print (False and False)
print (False and True)
print (True and False)
print (True and True)

# OU (or)
print (False or False)
print (False or True)
print (True or False)
print (True or True)

# Não (not)
print (not False)
print (not True)


#CONTROLE DE FLUXO 

# Se a condição for verdadeira faça (if)
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print ("a é maior que b") 
print ("Fim")

# Se a condição for verdadeira faça (if) senão faça (else)

altura = float(input("Digite a sua altura: "))
if altura > 1.6:
    print("Você pode subir! :)")
else:
    print("Você não pode subir! :(")

# CONDICIONAL EM CASCATA

#Estrutura condicional
# 1 if
# 0 ou n elifs
# 0 ou 1 else

media = float(input("Digite a media: "))

if media >=5:
    print("Aprovado")

elif media >=3:
    print("Recuperação")

else:
    print("Reprovado")