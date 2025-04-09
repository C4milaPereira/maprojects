import os

from Funcao import listar_imoveis, menu, cadastroimovel, visitar_imovel, saudacao, voltarmenu, alugar_imovel

while True:
    opcao = menu()
    if opcao == 1:
        cadastroimovel()
        if not voltarmenu():
            saudacao()
            break
    elif opcao == 2:
        listar_imoveis()
        visitar_imovel()
        if not voltarmenu():
            saudacao()
            break
    elif opcao == 3:
        listar_imoveis()
        alugar_imovel()
        if not voltarmenu():
            break
    elif opcao == 0:
        saudacao()
        break
    else:
        print("Opção inválida, tente novamente.")
