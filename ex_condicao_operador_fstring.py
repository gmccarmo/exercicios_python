"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
    Seu nome é {nome} FEITO
    Seu nome invertido é {nome[::-1]} FEITO
    Seu nome contém (ou não) espaços FEITO
    Seu nome tem print(len(nome)) letras FEITO
    A primeira letra do seu nome é {nome[0]} FEITO
    A última letra do seu nome é {nome[(len(nome)]} FEITO
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Entre com o seu nome: ')
idade = input('Entre com a sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')

else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
        
    print(f'Seu nome contém ',len(nome),' letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[(len(nome)-1)::]}')
