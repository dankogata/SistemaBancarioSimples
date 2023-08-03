
contador =0
extrato =0
i=0
menu ="""
[u] Criar usuário
[cc] Criar conta corrente
[s] saque
[d] Depositar
[e] Extrato
[q] Sair
"""


def deposito(v1,extrato):
    v1=float(input("Qual o valor de deposito:"))
    extrato += v1
    
def saque(v2,extrato):
    v2=float(input("qual o valor o saque:"))
    i=0
    if v2 <500:
        extrato -= v2
        i+=1
    elif i<3:
        print("limite de saques diários ultrapassados")
    else:
        print("valor acima do permitido")
 
 
#TODOs
#CRIAR FUNÇÃO DE CRIAR USUÁRIOS E CONTA CORRENTE + refatorar   
while True:
    opcao = input(menu)
    if opcao == "d":
        deposito= float(input("Qual o valor do deposito: "))   
        if deposito>0:
            extrato += deposito
            contador+=1
        else:
            print ("valor incorreto")
           
    elif opcao == "e":
        print("\n=================EXTRATO==================")
        print(f"Foram feitas {contador} movimentações \n")
        print(f"O saldo da conta é de: R$ {extrato} \n", )
        print("Sistema finalizado com sucesso")
        print("\n==========================================")
        break
    
    elif opcao == "s":
        saque= float(input("Qual o valor do saque: "))
        if saque>500:
            print("Valor acima do permitido")
        elif i<3:
            extrato -= saque
            i+=1
            contador+=1
        else:
            print("Limite de saques diários permitidos")   
       
    elif opcao=="cc":
        contaCorrente=list(input("Digite o nº de conta corrente desejado:"))
        break
           
    elif opcao=="u":
        nome=list(input("Qual o seu nome:"))
        break
           
    elif opcao == "q":
        print("Sistema finalizado com sucesso")
        break