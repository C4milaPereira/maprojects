import os

from Funcao import listar_imoveis, menu, cadastroimovel, alugarimovel, saudacao, voltarmenu

while True:
    opcao = menu()
    if opcao == 1:
        cadastroimovel()
        if not voltarmenu():
            saudacao()
            break
    elif opcao == 2:
        listar_imoveis()
        alugarimovel()
        if not voltarmenu():
            saudacao()
            break
    elif opcao == 0:
        saudacao()
        break
    else:
        print("Opção inválida, tente novamente.")
