from Funcao import listar_imoveis, menu, cadastroimovel, alugarimovel, voltarmenu

while True:
    opcao = menu()
    if opcao == 1:
        cadastroimovel()
    elif opcao == 2:
        listar_imoveis()
        alugarimovel()
        if voltarmenu():
            continue
    elif opcao == 0:
        print("Obrigada por usar nossos serviços!")
        break
    else:
        print("Opção inválida, tente novamente.")
