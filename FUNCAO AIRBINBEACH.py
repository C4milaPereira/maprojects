import os

imoveis = [
    {"Localizacao": "Sol, Rua Solar, 202", "Diaria": "250", "Status": "Disponível"},
    {"Localizacao": "Lua, Rua Minguante, 101", "Diaria": "200", "Status": "Disponível"}
]

def menu():
    os.system("cls")  # Limpa a tela
    print("AIRBINBEACH\n")
    print("1 - Cadastrar um imóvel")
    print("2 - Alugar um imóvel")
    print("0 - Sair")
    opcao = int(input("Selecione a opção desejada: "))
    return opcao


def cadastroimovel():
    while True:
        print("CADASTRAR IMÓVEL")
        imovel_cad = {"Localizacao": "", "Diaria": "", "Status": "Disponível"}
        imovel_cad["Localizacao"] = input("Onde fica localizado o imóvel: ")
        imovel_cad["Diaria"] = input("Qual o valor da diária: ")
        imoveis.append(imovel_cad)
        print("O imóvel foi cadastrado com sucesso!")

        resp = input("Deseja cadastrar mais algum imóvel? (sim/não) ").lower()
        if resp != "sim":
            break


def voltarmenu():
    resp1 = input("Deseja voltar ao menu? (sim/não) ").lower()
    if resp1 in ["sim", "não"]:
        return resp1 == "sim"
    else:
        print("Resposta inválida, digite apenas sim ou não")

def listar_imoveis():
    print("TODOS OS IMÓVEIS:")
    for i, imovel_cad in enumerate(imoveis):
        print(
            f"{i+1}. Localização: {imovel_cad['Localizacao']}, Diária: {imovel_cad['Diaria']}, Status: {imovel_cad['Status']}")
    
def alugarimovel(): 
    escolha = int(input("Qual imóvel deseja locar? "))
    if 1 <= escolha <= len(imoveis):
        if imoveis[escolha - 1]["Status"] == "Disponível":
            imoveis[escolha - 1]["Status"] = "Indisponível"
            print(f"O imóvel {escolha} foi alugado com sucesso!")
            print("Obrigada pela preferência! :)")
        else:
            print("Desculpe, este imóvel está indisponível.")
    else:
        print("Número inválido, tente novamente.")
