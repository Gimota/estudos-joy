#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

continuar = "sim"
while continuar == "sim":

    PrimeiroNumero= int(input("digite o primeiro numero"))
    SegundoNumero= int(input("Digite o segundo numero"))

    TipoOperacao= input("Digite a operacao a ser usada. digite 1 para soma, digite 2 para subtracao, digite 3 para multiplicacao, digite 4 para divisao e 0 para opcao sair")

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
    elif(TipoOperacao=="0"):
        continuar="nao"
        break
    else:
        Resultado = 0
    
    print ("resultado igual a:", Resultado)
    continuar = input("Deseja continuar? (sim/nao)")