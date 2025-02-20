def mostrar_menu():
    print("\n=== Calculadora ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calcular(opcao, num1, num2):
    if opcao == 1:
        return num1 + num2
    elif opcao == 2:
        return num1 - num2
    elif opcao == 3:
        return num1 * num2
    elif opcao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero."
    else:
        return "Opção inválida."

while True:
    mostrar_menu()
    
    opcao = int(input("\nEscolha uma opção: "))
    
    if opcao == 5:
        print("Encerrando a calculadora.")
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = calcular(opcao, num1, num2)
    print("Resultado:", resultado)
    
    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando a calculadora.")
        break