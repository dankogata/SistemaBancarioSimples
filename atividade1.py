#TODOs
#CRIAR FUNÇÃO DE CRIAR USUÁRIOS E CONTA CORRENTE + refatorar   

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
listaContas=[]
listaNomes=[]

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
        contaCorrente=input("Digite o nº de conta corrente desejado:")
        listaContas.append(contaCorrente)
        print(listaContas)
           
    elif opcao=="u":
        nome=input("Qual o seu nome:")
        listaNomes.append(nome)
        print(listaNomes)
           
    elif opcao == "q":
        print("----------Sistema finalizado com sucesso----------")
        break