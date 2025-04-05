
# Exercicio Numero 1

# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}! Seja Bem vindo")


# Execicio Numero 2

# numero= int(input("Digite o numero: "))
# if numero%2 == 0 :
#    print("Esse Numero é par")
# else:
#    print("Esse Numero é impar")

# Exercicio Numero 3
# Exemplo mais facil exercicio 3
# lista=[]
# for i in range(0,3):
#     i= input("Digite seu nome: ")
#     lista.append(i)
# print(lista)
# for n in lista:
#   print(n)


# Meu Exercicio abaixo

# lista=[]
# nome1 =input(f"Digie o {i}º na lista: ")
# nome2 =input(f"Digie o {i}º na lista: ")
# nome3 =input(f"Digie o {i}º na lista: ")
# lista.append(nome1)
# lista.append(nome2)
# lista.append(nome3)
# print(lista)
# for n in lista:
#   print(n)



# Exercicio Numero 4

def adiciona_nome(lista):
      lista.append(input("Digite seu nome: "))
      print(lista)

def remove_nome(lista):
    lista.pop()
    print(lista)


menu= 1
lista=[]
while menu== 1:
    print("O que quer fazer?")
    print("1. Adicionar nomes")
    print("2. Remover Nomes")

    escolha= int(input("Digite uma ação: "))

    if escolha == 1 :
        adiciona_nome(lista)
        menu+1
    elif escolha == 2:
        remove_nome(lista)
        menu+1
    else:
        print("Digite os numeros de acordo as opções acima")


