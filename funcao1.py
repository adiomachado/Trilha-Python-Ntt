def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
num1 = float(input("primeiro numero: "))
num2 = float(input("segundo numero: "))


exibir_resultado(num1, num2, somar)  # O resultado da operação 10 + 10 = 20