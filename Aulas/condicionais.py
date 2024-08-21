print("Bem vindo, siga as instruções para conferir se você pode entrar: ")

nome = (input("Digite seu nome: "))

idade = int(input("Digite sua idade: "))


if idade >= 18:
    print("PERMITIDO")
else:
    print("NÃO PERMITIDO!")