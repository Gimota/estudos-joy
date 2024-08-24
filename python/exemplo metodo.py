
continuar = "sim"
def escrever_multiplicacao(num1,num2):
    resultado= str(num1 * num2)
    frase = str(num1)+ "*" + str(num2)+ "=" + resultado
    return frase

while continuar == "sim":
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite outro numero: "))

    print(escrever_multiplicacao (numero1,numero2))
    continuar = input("Deseja continuar? (sim/nao)")