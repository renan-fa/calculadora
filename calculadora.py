import math as mt

def numeros():

    n = float(input("Digite o número: "))
    return n

def adicionar(a, b):

    return a + b 

def subtrair(a, b):

    return a - b

def multiplicar(a, b):

    return a * b

def dividir(a, b):

    return a / b 

def exponenciacao(a, b):

    return a ** b

def radiciacao(a):

    raiz = mt.sqrt(a)
    return raiz

def porcentagem(a, b):

    return a * (b/100)

def fatorial(a):

    resultado = 1
    count = 1

    while count <= a:

        resultado *= count
        count += 1


    return resultado
    

def calculadora():

    print("Selecione a operação.")
    print("1.Adição")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    print("5.Exponenciação")
    print("6.Radiciação")
    print("7.Porcentagem")
    print("8.Fatorial")

    escolha = input("Digite a opção (1/2/3/4/5/6/7/8): ")

    if escolha == '1':

        num1 = numeros()
        num2 = numeros()
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
        
    elif escolha == '2':

        num1 = numeros()
        num2 = numeros()
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")

    elif escolha == '3':

        num1 = numeros()
        num2 = numeros()
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

    elif escolha == '4':

        num1 = numeros()
        num2 = numeros()
        print(f"{num1} / {num2} = {dividir(num1, num2)}")

    elif escolha == '5':

        num1 = numeros()
        num2 = numeros()
        print(f"{num1} ** {num2} = {exponenciacao(num1, num2)}")

    elif escolha == '6':
        
        num1 = numeros()
        raiz = radiciacao(num1)
        print(f"Raiz quadrada de {num1} = {raiz}")

    elif escolha == '7':

        num1 = numeros()
        num2 = numeros()
        print(f"{num2}% de {num1} é igual = {porcentagem(num1, num2)}")

    elif escolha == '8':

        num1 = numeros()
        print(f"Fatorial do numero {num1} é = {fatorial(num1)}")

    else:

        print("Opção inválida")


if __name__ == "__main__":
    calculadora()
