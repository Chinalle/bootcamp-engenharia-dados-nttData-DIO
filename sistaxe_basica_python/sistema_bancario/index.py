# Menu:
    # Não precisa identificar qual é o número da agência e conta bancária
    # Deve conter as opções Depósitos, Saques e Extrato

# Depósitos:
    # Depositar apenas valores positivos
    # Todos os depositos devem ser armazenados em uma variável e exibidos na operação extrato

# Saques:
    # Deve permitir 3 saques diários com limite máxima de R$ 500,00 por saque.
    # Caso não tenha dinheiro em conta, o sistema deve exibir uma mensagem informando
    # Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato:
    # Deve listar todos os depósitos e saques realizados na conta
    # No fim da listagem deve ser exibido o saldo atual da conta
    # Os valores devem ser exibidos no formato  R$ xxx.xx -> R$ 1500.45

'''
FALTA TESTAR E SUBIR NO GIT

'''

saldo_conta = 0
limite_saque_qtd = 3
limite_saque_valor = 500.00
extrato = []
def menu():
    print("Sistema Bancário".center(48,'='))
    print('''
        [D] Depositar
        [S] Saques
        [E] Extratos
        [Q] Sair
        ''')
    
def operacoes():
    global saldo_conta
    global extrato
    global limite_saque_qtd
    global limite_saque_valor
    while True:
        menu()
        operacao = input("Opção:")

        if operacao == 'D':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            if valor_deposito > 0.0:
                saldo_conta += valor_deposito
                extrato.append(valor_deposito)
                print("Valor Depositado com sucesso!!")
            else:
                print("Valores menores ou iguais a zero, não é possível realizar o depósito!!")
            
        
        elif operacao == 'S':
            valor_sacar = float(input("Digite o valor a ser sacado: "))
            if valor_sacar > 0.0 and valor_sacar <= limite_saque_valor and valor_sacar <=saldo_conta and limite_saque_qtd !=0:
                saldo_conta-=valor_sacar
                valor_extrato_saque = valor_sacar*(-1)
                extrato.append(valor_extrato_saque)
                limite_saque_qtd -= 1
                print("Saque realizado com sucesso!!")

            elif valor_sacar > limite_saque_valor:
                print(f"O valor a ser sacada de {valor_sacar} é maior que o limite por saque de {limite_saque_valor}!!")
            
            elif valor_sacar <=0:
                print("Valores menores ou iguais a zero, não é possível realizar o depósito!!")

            elif valor_sacar > saldo_conta:
                print(f"O valor a ser sacada de {valor_sacar} é maior que o valor disponível na sua conta!!")
                print("Consulte seu extrato!!")

            elif limite_saque_qtd == 0:
                print(f"Você ja realizou a quantidade de saque permitida de {limite_saque_qtd} vezes ao dia!!")       

        elif operacao == 'E':
            if len(extrato) > 0:
                for transacao in extrato:
                    print(f"R$ {transacao}")
            else:
                print("Nenhuma operação registrada!!")
            print(f"SALDO EM CONTA: R$ {saldo_conta}")
        
        elif operacao == 'Q':
            break

        else:
            print("Nenhuma dessas opções correspondem as operações exibidas no menu \n")

operacoes()
