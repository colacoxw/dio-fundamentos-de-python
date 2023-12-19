def sacar(valor: float):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado")
    else:
        print("Saldo insuficiente!")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor: float):
    saldo = 500
    saldo += valor


sacar(1000)