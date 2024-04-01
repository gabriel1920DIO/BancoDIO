import os 
operacao = 0
op = ""
saldo = 0
bb = True

def sacar():
    global saldo
    os.system("cls")
    operacao = float(input("Digite quanto você quer sacar: "))
    saldo -= operacao
    os.system("cls")

def dep():
    os.system("cls")
    global saldo
    operacao = float(input("Digite quanto você quer depositar: "))
    saldo += operacao
    os.system("cls")

def hist():
    os.system("cls")
    print("Saldo atual:", saldo)
          
while op != 'q':
    print(f"seu saldo: {saldo:.2f}")
    op = input("Olá, bem-vindo ao Banco Santander! Qual operação deseja fazer?\n[d]epositar\n[s]aque\n[e]xtrato\n[q]sair\n")
    op = op.lower()
    if op == "d":
        dep()
    elif op == "s":
        sacar()
    elif op == "e":
        hist()
    else:
        print("Responda com uma opção válida.")

print("Obrigado por usar o programa!")
