def manipular_estoque(arr):
  fechar= False
  while (fechar == False):
    print("a lista de produtos que trabalharemos é", arr)
    print("o que vc deseja fazer?" + "digite o numero")
    print("1 - adicionar produto")
    print("2 - remover produto")
    print("3 - alterar produto")
    print("4 - sair")
    acao = input()

    if(acao == "1"):
      produto=input("Digite o novo produto: ")
      arr.append(produto) 
      print("A lista de produtos atualizada é ", arr)

    elif(acao == "2"):
      print("Qual é o produto que deseja remover? ")
      produto = str(input())
      arr.remove(produto)
      print("A lista de produtos atualizada é ", arr)

    elif(acao=="3"):
        print("Qual é o produto do produto que deseja alterar? ")
        produto = str(input())
        print("Qual é o novo nome  do produto ? ")
        novoproduto  = str(input())
        arr.remove(produto)
        arr.append (novoproduto)
        print ("o novo lista de produtos  é ", arr)


    elif(acao == "4"):
        print("Fechando o sitema")
        fechar = True

    else:
      print("Por favor informe um código válido")

produtos = ["açai", "pão", "manteiga", "arroz","queijo"]

manipular_estoque(produtos)



produtos2 = ["ferro", "areia", "cimento", "pedra","tijolo"]

manipular_estoque(produtos2)