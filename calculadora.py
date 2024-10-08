# Definição da função adicionar, que irá somar dois números.
def adicionar(a, b):
    return a + b # soma o primeiro numero com o segundo

# Definição da função subtrair, que será responsável por subtrair o segundo número do primeiro.
def subtrair(a, b):
    return a - b # subtrai o pimeiro numero pelo segundo

# Definição da função multiplicar, que multiplicará dois números.
def multiplicar(a, b):
    return a * b # multiplica o primeiro pelo segundo numero

# Definição da função dividir, que fará a divisão do primeiro número pelo segundo.
# O tratamento de divisão por zero foi adicionada em outra parte do código
def dividir(a, b):
    return a / b # divide o primeiro numero pelo segundo

# Definição da função potência, que fará a potenciação do primeiro numero pelo segundo
def potencia(a, b):
    return a ** b # calcula a potência do primeiro numero pelo segundo

# Função principal da calculadora, responsável por interagir com o usuário e realizar operações.
def calculadora():
    # Exibe as opções de operação disponíveis para o usuário escolher.
    print("Selecione a operação.")
    print("1.Adição")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    print("5.Potência")

    # Recebe a escolha da operação do usuário.
    escolha = input("Digite a opção (1/2/3/4/5): ")

    # Solicita dois números do usuário e converte-os para o tipo float.
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Verifica qual operação foi selecionada pelo usuário.
    if escolha == '1':
        # Se o usuário escolheu adição, chama a função adicionar com os números inseridos e exibe o resultado.
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
    elif escolha == '2':
        # Se o usuário escolheu subtração, chama a função subtrair e exibe o resultado.
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        # Se o usuário escolheu multiplicação, chama a função multiplicar e exibe o resultado.
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        # Se o usuário escolheu divisão, chama a função dividir e exibe o resultado.    
        # Foi adicionado um tratamento de erro caso tente dividir por zero
        if num2 == 0:
            print("Nao e possivel dividir um numero por zero")
            print(f"{num1} / {num2}")

        else:    
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    elif escolha == '5':
        # Se o usuario escolheu potenciação, chama a função de potência e exibe o resultado
        print(f"{num1} ** {num2} = {potencia(num1, num2)}")        
    else:
        # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro.
        print("Opção inválida")

# Bloco principal, que executa a função 'calculadora' quando o script é executado diretamente.
if __name__ == "__main__":
    calculadora()
