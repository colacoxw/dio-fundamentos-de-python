def verificar_encaixe(a, b):
    return 'encaixa' if a.endswith(b) else 'nao encaixa'

def main():
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        resultado = verificar_encaixe(a, b)
        print(resultado)

main()
