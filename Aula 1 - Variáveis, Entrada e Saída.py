### Passos de um programa
# Entrada
# Processamento
# Saída

### Saída
# Comando(função) print, imprime o que estiver entre parênteses
print("Olá, mundo")

nome = "Victor"
print("Olá", nome)

### Tipos de Variáveis
# Inteiros(int)
x = 10
print(x)

# Reais(float)
y = 3.2
print(y)

# Strings(str)
nome = "Victor"
print(nome)

# Booleano(bool)
a = True
b = False
print(a, b)

# Em python, não existe problema em mudar o tipo de uma variável
x = 10
print(x)
x = "Oi"
print(x)

### Operadores matemáticos
x = 5
y = 3
# Soma(+)
print(x+y)
# Subtração(-)
print(x-y)
# Multiplicação(*)
print(x*y)
# Divisão(/)
print(x/y)
# Divisão inteira(//)
print(x//y)
# Resto da divisão inteira(%)
print(x%y)
# Potenciação(**)
print(x**y)

### Entrada
# Função input, mostra na tela o que estiver entre parênteses, e retorna o que a pessoa digitar
idade = input("Digite a sua idade: ")
print("A sua idade é", idade)

# A função input sempre retorna uma string, então se
# queremos outro tipo de variável, precisamos converter
int(idade) # Converte a variável idade para um número inteiro 

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print("A soma é", a+b)

x = int(input("Digite um número: "))
print("O quintuplo é:", 5*x)
