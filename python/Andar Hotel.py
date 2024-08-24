#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#declara variavel com total de andares para uso no exercicio com while
totalandarComWhile = 20

#inicia o laco de repeticao while que enquanto o andar for maior que zero, ele vai executar o codido abaixo dele
while(totalandarComWhile>0):
    #verifica se o andar é diferente de 13
    if totalandarComWhile != 13:
        #se for diferente de treze, ele vai imprimir andar atual, concatenando o andar
        print ("Andar atual:", totalandarComWhile)
        #subtrai 1 do andar para ir ao proximo
        totalandarComWhile=totalandarComWhile-1
    #entra so no caso do andar ser 13    
    else:
          #subtrai 1 do andar para ir ao proximo
        totalandarComWhile=totalandarComWhile-1
   

#declara lista de andares (array)
andares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

andares.sort(reverse=True)

#inicia o laco de repeticao for que ira percorrer toda a lista de numeros com andares
for n in andares:
    #verifica se o andar é diferente de 13
    if n != 13:
        #se for diferente de treze, ele vai imprimir andar atual, concatenando o andar
        print ("Andar atual:", n)
