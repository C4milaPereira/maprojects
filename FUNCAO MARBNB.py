import os

id_locador = 3
id_imovel = 3

locadores = [
    {"id": 1, "Nome": "Manuel Oliveira Santos",
        "Contato": "(11)2022-3542", "Email": "manueloliver@yahoo.com"},
    {"id": 2, "Nome": "Marcia Goncalves",
     "Contato": "(11)2032-2852", "Email": "magoncalves@yahoo.com"}
]
imoveis = [
    {"Localizacao": "Rua Solar, 202, Praia dos Anjos", "Mensal": 1.800,
        "Status": "Disponível", "id_locador": 1},
    {"Localizacao": "Rua Minguante, 101, Pontal do Atalaia", "Mensal": 5.000,
        "Status": "Disponível", "id_locador": 2}
]

def saudacao():
    print("Obrigada por usar nossos serviços! :)")

def menu():
    print("MARBNB 🌴🏡 ALUGUEL DE CASAS NA PRAIA")
    print("1 - Cadastrar um imóvel")
    print("2 - Alugar um imóvel")
    print("0 - Sair")
    opcao = int(input("Selecione a opção desejada: "))
    return opcao


def cadastroimovel():
    global id_locador, id_imovel, imoveis, locadores
    print("CADASTRAR IMÓVEL")
    print("DADOS LOCADOR:")
    dados_locador = {
        "id": id_locador,
        "Nome": input("Nome: "),
        "Contato": input("Telefone: "),
        "Email": input("Email: ")
    }
    locadores.append(dados_locador)
    id_locador += 1

    imovel_cad = {
        "id": id_imovel,
        "Localizacao": input("Onde fica localizado o imóvel: "),
        "Mensal": float(input("Qual o valor do aluguel: ").replace(",", ".")),
        "Status": "Disponível",
        "id_locador": dados_locador["id"]
    }
    imoveis.append(imovel_cad)
    id_imovel += 1
    print("O imóvel foi cadastrado com sucesso!")


def voltarmenu():
    resp1 = input("Deseja voltar ao menu? (sim/não) ").lower()
    if resp1 == "sim":
        return True
    elif resp1 == "não":
        return False


def listar_imoveis():
    print("TODOS OS IMÓVEIS:")
    for imovel in imoveis:
        print(
            f"ID: {imovel['id_locador']}. Localização: {imovel['Localizacao']}, Mensal: {imovel['Mensal']}, Status: {imovel['Status']}")


def alugarimovel():
    escolha = int(input("Digite o numero do imóvel qual deseja visitar: "))
    if 1 <= escolha <= len(imoveis):
        imovel_select = imoveis[escolha - 1]
        if imovel_select["Status"] == "Disponível":
            imovel_select["Status"] = "Indisponível"
            os.system("cls")
            print(f"Aqui estão os dados para agendar sua visita:")
            print(
                f"\nDADOS IMÓVEL: \n{imovel_select['id_locador']}. Endereço: {imovel_select['Localizacao']} \nValor do imóvel: R${imovel_select['Mensal']:.3f}")
            locador = next(
                (locador for locador in locadores if locador['id'] == imovel_select['id_locador']), None)
            if locador:
                print(
                    f"\nCONTATO DO LOCADOR: \nNome: {locador['Nome']} \nTelefone: {locador['Contato']} \nEmail: {locador['Email']}\n")
                print("Obrigada pela preferência! :)")
        else:
            print("Desculpe, este imóvel está indisponível.")
    else:
        print("Número inválido, tente novamente.")
