
#declara variaveis e atribui valores para ela
bebida_nome = "gyn"
bebida_preco = 20
alcoolica = True

# escreve na tela nome da bebida atribuida na variavel bebida_nome
print(bebida_nome)

# escreve na tela preco da bebida atribuida na variavel bebida_preco
print(bebida_preco)

#escreve na tela se a bebida é alcolica com valor atribuido na variavel alcoolica
print(alcoolica)

#escreve na tela uma mensagem amigavel concatenando nela as variaveis criadas onteriormente (bebida_nome e bebida_preco)
print("minha bebida favorita é", bebida_nome, "seu preco é", bebida_preco)

#declara variavel almoco_favorito e atribui o valor de churrasco
almoco_favorito = "churrasco"

#declarando variavel preco_almoco e atribui o valor de 100
preco_almoco = 100

#escreve na tela uma mensagem amigavel concatenando nela as variaveis criadas onteriormente (almoco_favorito e preco_almoco)
print ("minha comida favorita e",almoco_favorito, "e o seu preco e", preco_almoco )

meuOrcamento = 200
#declara variavel orcamentoPedido e atribui para ela a soma dos valores de bebida_preco + preco_almoco, ambas já agtribuidas anteriormente
orcamentoPedido = bebida_preco + preco_almoco

#verifica se o orcamento é suficiente e escreve se é ou nao suficiente
if(orcamentoPedido < meuOrcamento):
    print("Seu orcamento é suficiente, compra aprovada.")
else:
    print ("seu orcamento é insuficiente.")
    