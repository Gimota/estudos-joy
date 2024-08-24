#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

PrimeiroNumero= int(input("digite o primeiro numero"))
SegundoNumero= int(input("Digite o segundo numero"))

TipoOperacao= input("Digite a operacao a ser usada. digite 1 para soma, digite 2 para subtracao, digite 3 para multiplicacao e digite 4 para divisao")

Resultado=0 


if(TipoOperacao=="1"):
    Resultado = PrimeiroNumero+SegundoNumero
    print ("resultado igual a:", Resultado)
elif (TipoOperacao=="2"):
    Resultado = PrimeiroNumero-SegundoNumero
    print ("resultado igual a:", Resultado)
elif(TipoOperacao=="3"):
    Resultado= PrimeiroNumero*SegundoNumero
    print ("resultado igual a:", Resultado)
elif(TipoOperacao=="4"):
    Resultado=PrimeiroNumero/SegundoNumero
    print ("resultado igual a:", Resultado)
else:
   Resultado = 0
   print ("resultado igual a:", Resultado)