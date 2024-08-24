#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2023.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2024).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

from datetime import datetime

NomeCompleto= input("digite seu nome completo")
AnoNascimento= input("Digite o seu ano de nascimento")

if AnoNascimento.isdigit():
    # Converte a string para inteiro
    AnoNascimento = int(AnoNascimento)
else:
    print("Entrada inválida. Por favor, digite um número.")
    exit

if(AnoNascimento>1922):
    anoAtual = datetime.now().year
    idade = anoAtual - AnoNascimento
    print(NomeCompleto + "tem " + str(idade) + " anos")
else:
    print("Ano de nascimenro invalido")
