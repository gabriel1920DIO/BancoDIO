#projeto banco
import os
saque = 0
limites = 3
saldo = 0
adcional = 0 
op =""
while op != "q":
 op= input(" olá bem vindo ao banco santander, que operaçao deseja fazer? \n [d]epositar \n [s]aque \n [e]xtrato \n [q]sair \n ")
 op = op.lower()
 os.system("cls")
 if op == 'd':
  dep = int(input("quanto deseja depositar"))
  saldo += dep
  print(f'seu saldo R${saldo:.2f}')
 elif op == "s": 
  sac = int(input('quanto deseja sacar? '))
  
  if limites > 0:
   saldo -= sac
   limites -= 1
   print(f'seu saldo R${saldo:.2f}')
  else: 
   print("limites de saques diarios atingididos ")
 elif op == "e":
  print(f'seu saldo R${saldo:.2f}')

os.system("cls")
print("obrigado por usar nosso banco")
