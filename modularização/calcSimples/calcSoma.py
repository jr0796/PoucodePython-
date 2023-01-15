import soma
import subtracao
import multiplicacao
import divisao
#Identação automática com a combinação CTRL+ALT+l

while True:

    texto= """
        1 - Para soma 
        2 - Para Subtração
        3 - Para Multiplicação
        4 - Para Divisão 
        5 - Sair
     """
    print (texto)
    print('Escolha uma operação ')
    try:
        escolha = int(input())

        if escolha == 1:
            print('ESCOLHA SOMA')
            print()
            print(f'O resultado será : {soma.soma(0, 0)}')
            input()

        elif escolha == 2:
            print('ESCOLHA SUBTRAÇÃO')
            print()
            print(f'O resultado será : {subtracao.sub(0, 0)}')
            input()

        elif escolha == 3:
            print('ESCOLHA MULTIPLICAÇÃO')
            print()
            print(f'O resultado será : {multiplicacao.mult(0, 0)}')
            input()

        elif escolha == 4:
            print('ESCOLHA DIVISÃO')
            print()
            print(f'O resultado será : {divisao.div(0, 0)}')
            input()

        elif escolha == 5:
            print('ESCOLHA SAIR')
            print()
            print('Obrigado por utilizar nossos produtos!')
            print(30 * '=')
            break
        else:
            print('Escolha inválida!')
            print('Por favor digite uma opção válida.')
            print(30 * '=')
            input()

    except ValueError:
            print('Escolha inválida!')
            print('Por favor digite uma opção válida.')
            print(30 * '=')
            input()






