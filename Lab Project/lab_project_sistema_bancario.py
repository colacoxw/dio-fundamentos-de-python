menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if(opcao == "d"):
    deposito = int(input("Quanto deseja depositar? \n"))
    if deposito > 0:
      saldo += deposito
      extrato += f"Depositado o valor de R$ {deposito} \n"
      print("Deposito realizado com sucesso!")        
    else:
        print("Não é possivel depositar este valor!")

  elif(opcao == "s"):
    if numero_saques >= LIMITE_SAQUES:
      print("Limite de saques foi atingido! Tente novamente outro dia.")
      continue
    else:
      numero_saques += 1
      saque = int(input("Quanto deseja sacar? \n"))
      if saque > limite:
        print("É possivel sacar no máximo R$ 500 por vez, tente novamente \n")
        continue
      else:
        if saque > saldo:
          print(f"Valor do saque R$ {saque} é superior ao saldo da sua conta R$ {saldo}, tente novamente!")
          continue
        else:
          saldo -= saque
          extrato += f"Saque no valor de R$ {saque} \n"
          print("Saque realizado com sucesso!") 
  elif(opcao == "e"):
    print(f"Saldo: {saldo} \n Movimentações: \n {extrato}")

  elif(opcao == "q"):
    break

  else:
    print("Erro, tente novamente")