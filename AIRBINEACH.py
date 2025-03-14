from Funcao import menu, cadastroimovel, voltarmenu, alugarimovel

while True:
    opcao = menu()
    
    if opcao == 1:
        cadastroimovel()
        resp = input("Deseja cadastrar mais algum imóvel? (sim/não) ").lower()
        while resp == "sim":
            cadastroimovel()
            resp = input("Deseja cadastrar mais algum imóvel? (sim/não) ").lower()
    elif opcao == 2:
        alugarimovel()
    elif opcao == 0:
        print("Obrigada por usar nossos serviços!")
        break
    else:
        print("Opção inválida, tente novamente.")
    
    if not voltarmenu():
        print("Fechando o programa... Até logo!")
        break