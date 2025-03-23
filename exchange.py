from datetime import datetime
from random import uniform
 
dados = {}
saldo = 0
valor = 0
extrato = []
bitcoin = []
ethereum = []
ripple = []
data = datetime.now()
valorBitcoin = 360058
valorETH = 19332
valorXRP = 2.78

def menu():
    print("""
          1 - Consultar saldo
          2 - Consultar extrato
          3 - Depositar
          4 - Sacar
          5 - Comprar Criptomoedas
          6 - Vender Criptomoedas
          7 - Atualizar Cotações
          8 - Sair""")

def cadastro():
    print("Cadastre-se!")
    d = {}
    cpf = input("Digite seu CPF: ")
    
    while len(cpf) != 11:
        print("CPF incorreto, tente novamente!")
        cpf = input("Digite seu CPF: ")
    d["senha"] = input("Crie uma senha: ")
    
    while len(d["senha"]) != 6:
        print("A senha deve conter 6 dígitos!")
        d["senha"] = input("Senha: ")
    
    d["nome"] = input("Digite seu nome: ")
    d["cpf"] = cpf 
    
    dados[cpf] = d
    return d

def login():
    print("Realize seu login") 
    cpf = input("Digite seu CPF sem pontos ou traços: ")
    while cpf not in dados:
        print("CPF não cadastrado. Por favor, cadastre-se.")
        cadastro()
        cpf = input("Digite seu CPF novamente: ")
    
    senha = input("Senha: ")

    if dados[cpf]["senha"] == senha:
        print("Login realizado com sucesso")
        if 'cpf' not in dados[cpf] or 'nome' not in dados[cpf]:
            dados[cpf]["cpf"] = cpf
            dados[cpf]["nome"] = input("Digite seu nome: ")
        return dados[cpf]
    else:
        return "Senha incorreta. Tente novamente."

def formata_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def consultar_saldo(usuario):
    global saldo
    saldo_info = ""
    saldo_info += f"Nome: {usuario['nome']} \n"
    saldo_info += f"CPF: {formata_cpf(usuario['cpf'])} \n"
    saldo_info += "Carteira \n"
    saldo_info += f"Reais: {saldo:.2f} \n"
    saldo_info += f"Bitcoin: {sum(bitcoin)} \n"
    saldo_info += f"Ethereum: {sum(ethereum)} \n"
    saldo_info += f"Ripple: {sum(ripple)} \n"
    return saldo_info

def consultar_extrato():
    print("Extrato:")
    for contas in extrato:
        return contas

def deposito():
    global saldo, valor
    valor = float(input("Quanto você deseja depositar?: "))
    saldo += valor
    extrato.append(f"{data} + {valor:.2f} REAL CT: 0.0 TX 0.00 REAL {saldo:.2f} BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
    return f"Depósito realizado com sucesso, seu novo saldo é de {saldo}R$"

def saque():
    global saldo, valor
    valor = float(input("Quanto você deseja sacar?: "))
    if saldo >= valor:
        saldo -= valor
        extrato.append(f"{data} - {valor:.2f} REAL CT: 0.0 TX 0.00 REAL {saldo:.2f} BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
        return f"Saque realizado com sucesso, seu novo saldo é de {saldo}R$"
    else:
        return "Erro, você não possui saldo o suficiente para realizar essa transação"

def comprar_cripto():
    global saldo, valor
    print("Primeiramente, lembramos que cobramos uma taxa de compra para cada moeda:\nBitcoin: 2%\nEthereum: 1%\nRipple: 1% ")
    moeda = input("Qual moeda você deseja comprar?: ")
    qntd = int(input(f"Então você quer comprar {moeda}, selecione a quantidade: "))
    preco = 0
    if moeda.lower() == "bitcoin":
        preco = qntd * valorBitcoin
        if preco > saldo:
            return "Você não possui saldo o bastante para comprar esta quantidade de Bitcoins"
        else:  
            bitcoin.append(qntd)
            saldo -= preco + (preco * 0.02)
            extrato.append(f"{data} - {valor:.2f} REAL CT: 0.0 TX 0.02 REAL BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
            return f"Compra realizada com sucesso, agora você possui {sum(bitcoin)} Bitcoin"
    elif moeda.lower() == "ethereum":
        preco = qntd * valorETH
        if preco > saldo:
            return "Você não possui saldo o bastante para comprar esta quantidade de Ethereum"
        else:
            ethereum.append(qntd)
            saldo -= preco + (preco * 0.01)
            extrato.append(f"{data} - {valor:.2f} REAL CT: 0.0 TX 0.01 REAL {saldo:.2f} BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
            return f"Compra realizada com sucesso, agora você possui {sum(ethereum)} Ethereum"
    elif moeda.lower() == "ripple":
        preco = qntd * valorXRP
        if preco > saldo:
            return "Você não possui saldo o bastante para comprar esta quantidade de Ripple"
        else:
            ripple.append(qntd)
            saldo -= preco + (preco * 0.01)
            extrato.append(f"{data} - {valor:.2f} REAL CT: 0.0 TX 0.00 REAL {saldo:.2f} BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
            return f"Compra realizada com sucesso, agora você possui {sum(ripple)} Ripple"
    else:
        return "Não encontramos esta moeda no nosso exchange, por favor selecione uma das moedas que nós trabalhamos!"

def vender_cripto():
    global saldo, valor
    print("Primeiramente, lembramos que cobramos uma taxa de venda para cada moeda:\nBitcoin: 3%\nEthereum: 2%\nRipple: 1% ")
    moeda = input("Qual moeda você deseja vender?: ")
    qntd = int(input(f"Então você quer vender sua/suas {moeda}, selecione a quantidade: "))
    preco = 0
    if moeda.lower() == "bitcoin":
        preco = qntd * valorBitcoin
        if qntd > sum(bitcoin):
            return "Você não possui essa quantidade de bitcoins o suficiente para vende-las"
        else:
            if qntd <= bitcoin[0]:
                saldo += preco - (preco * 0.03)
                bitcoin[0] -= qntd
                extrato.append(f"{data} + {valor:.2f} REAL CT: 0.0 TX 0.03 REAL BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
                return f"Venda realizada com sucesso, agora você possui {sum(bitcoin)} bitcoins e {saldo:.2f}R$"
    elif moeda.lower() == "ethereum":
        preco = qntd * valorETH
        if qntd > sum(ethereum):
            return "Você não possui essa quantidade de Ethereum o suficiente para vende-las"
        else:
            if qntd <= ethereum[0]:
                saldo += preco - (preco * 0.02)
                ethereum[0] -= qntd
                extrato.append(f"{data} + {valor:.2f} REAL CT: 0.0 TX 0.02 REAL {saldo:.2f} BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
                return f"Venda realizada com sucesso, agora você possui {sum(ethereum)} ethereum e {saldo:.2f}R$"
    elif moeda.lower() == "ripple":
        preco = qntd * valorXRP
        if qntd > sum(ripple):
            return "Você não possui essa quantidade de Ripple o suficiente para vende-las"
        else:
            if qntd <= ripple[0]:
                saldo += preco - (preco * 0.01)
                ripple[0] -= qntd
                extrato.append(f"{data} + {valor:.2f} REAL CT: 0.0 TX 0.01 REAL {saldo:.2f} BTC: {sum(bitcoin):.2f} ETH: {sum(ethereum):.2f} XRP: {sum(ripple):.2f}")
                return f"Venda realizada com sucesso, agora você possui {sum(ripple)} ripples e {saldo:.2f}R$"
    else:
        return "Não encontramos esta moeda no nosso exchange, por favor selecione uma das moedas que nós trabalhamos!"         

def att_cota():
    global valorBitcoin, valorETH, valorXRP
    variacao_cripto = uniform(-0.05, 0.05)
    valorBitcoin += valorBitcoin * variacao_cripto
    valorETH += valorETH * variacao_cripto
    valorXRP += valorXRP * variacao_cripto
    return f"A cotação atual está em \n Bitcoin: {valorBitcoin:.1f} \n Ethereum: {valorETH:.1f} \n Ripple: {valorXRP:.1f}"

def arq_txt(texto):
    with open("exchange.txt", "a", encoding='utf8') as file:
        file.write(texto + "\n")

while True:
    entrada = int(input("Seja bem vindo(a), você deseja se cadastrar[1] ou fazer login[2]: "))
    arq_txt(str(entrada))
    if entrada == 1:
        dados_usuario = cadastro()
        arq_txt(str(dados_usuario))
    elif entrada == 2:
        usuario = login()
        arq_txt(str(usuario))
        while True:
            menu()
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                arq_txt(consultar_saldo(usuario))
            elif opcao == 2:
                arq_txt(consultar_extrato())
            elif opcao == 3:
                arq_txt(deposito())
            elif opcao == 4:
                arq_txt(saque())
            elif opcao == 5:
                arq_txt(comprar_cripto())
            elif opcao == 6:
                arq_txt(vender_cripto())
            elif opcao == 7:
                arq_txt(att_cota())
            elif opcao == 8:
                arq_txt("Obrigado por utilizar nosso exchange, volte sempre!")
                exit()
    else:
        print("Opção inválida, tente novamente")
