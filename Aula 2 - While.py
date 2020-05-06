### While
# Estrutura
# while condicao:
#     codigo a ser repetido

# While para validação de entrada
# Programa vai ficar pedindo novas entradas enquanto o seu valor não for válido
idade = int(input("Digite a sua idade: "))

while idade < 0 or idade > 200:
    print("Idade inválida")
    idade = int(input("Digite a sua idade: ")) # Atualiza o valor da variável
print("Fim")

# While com contador
i = 0 # Condição inicial
while i <= 100: # Condição de parada
    print(i)
    i += 1      # Incremento


