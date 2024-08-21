while True:
    x = int(input("Digite um número (ou 0 para sair): "))
    
    if x == 0:  # Verifica se o número é 0 para sair do loop
        print("Saindo...")
        break   # Sai do loop quando x é 0
    if x < 0:
        print("Número negativo")
    elif x > 0:
        print("Número positivo")
    
    if x % 2 == 0:
        print("E também é par")
    else:
        print("E também é ímpar")
