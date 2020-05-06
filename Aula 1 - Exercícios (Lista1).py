# Variáveis, Input/Output 

# 1. Faça um programa que mostre a mensagem "Olá, mundo!" na tela. 
print ("Olá, mundo!")

# 2. Faça um programa que peça um número e mostre a mensagem "O número informado foi [número]". 
num = int (input ("Digite um número: "))
print ("O número digitado foi:", num)

# 3. Faça um programa que peça um número para o usuário (string), converta-o para float e depois imprima-o na tela. Você consegue fazer a mesma coisa, porém convertendo para int? 
num = float (input("Digite um número: "))
print ("O número digitado foi: ", num)
print ("Convertido em inteiro: ", int(num))

# 4. Faça um programa que peça dois números e imprima a soma deles. 
a = int (input("Digite um número: "))
b = int (input("Digite outro número: "))
print ("A soma é: ", a+b)

# 5. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas. 
aluno = input ("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4

print ("A média do aluno ", aluno," é: ", media)
if media >=5:
    print("O aluno", aluno, "está APROVADO")
elif media >=3:
    print("O aluno", aluno, "está de RECUPERAÇÃO")
else:
    print("O aluno", aluno, "está REPROVADO")

# 6. Faça um programa que converta um valor em metros para centímetros. 
m = float (input("Digite o valor em metros: "))
cm = m*100
print ("O valor em centímetros é:",cm)

# 7. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
#Obs: Fórmula da área de um círculo: A = 3,14*r2, onde r é o raio.
r = float (input("Digite o raio de um círculo: "))
print ("A área do círculo é", 3.14*r**2)


# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês. 
valorHora = float (input("Insira o valor/hora: "))
horasTrabalhadas = float (input("Insira a quantidade de horas trabalhadas no referido mês:"))
print ("O valor do salário neste mês é: R$", valorHora*horasTrabalhadas)

# 9. Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C). 
# #°C = (5 * (F-32) / 9)
# Obs: Tente também fazer um programa que faça o inverso: peça a temperatura em graus Celsius e a transforme em graus Fahrenheit.

while 1:
       
    print ("Escolha uma opção de conversão\n1) Fahrenheit para Celsius \n2) Celsius para Fahrenheit ")
    selecao = input("Digite o número da opção desejada:")

    if selecao == "1":
        f = int (input("Insira o a temperatura em Fahrenheit: "))
        c = (5*(f-32)/9)
        print (f,"graus Fahrenheit equivalem a ",c,"ºC")
        
    elif selecao == "2":
        c = int (input("Insira o a temperatura em graus Celsius: "))
        f = (c*9/5)+32
        print (c,"ºC equivalem a ",f,"graus Fahrenheit")
        
    else:
        print ("Opção inválida")

# 10. Faça um programa que peça o dia, o mês e o ano para o usuário e imprima a data completa no formato dd/mm/aaaa. 

d= int(input("Digite o dia: "))
m= int(input("Digite o mês: "))
a= int(input("Digite o ano: "))

data = "%02d/%02d/%d" %(d,m,a)

print(data)

# 11. Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

# 12. Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).
# Obs: IMC = Peso/Altura2

# 13. Faça um programa que peça um valor monetário e aumente-o em 15%.
# Seu programa deve imprimir a mensagem “O novo valor é R$[valor]”.

# 14. Faça um programa que peça um valor monetário e diminua-o em 15%.
# Seu programa deve imprimir a mensagem “O novo valor é R$[valor]”. 

# Desafios 

# 1. Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo.
# Dica: use a fórmula matemática y(t) = y(0) + v(0) * (t + (g*t^2)/2) 

# Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.

# ian