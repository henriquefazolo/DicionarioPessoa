'''
Crie um dicionário que guarde as seguintes informações de uma pessoa: nome, cpf, telefone e endereço.
'''

pessoa1 = {'nome': 'João', 'cpf': '12345678900', 'telefone': '+55 43 9 99999999', 'endereço': 'Rua dos bobos nº 0'}


'''
Crie uma lista de dicionários que guarde as seguintes informações de uma pessoa: nome, cpf, telefone e endereço.
'''

pessoa1 = {'nome': 'João', 'cpf': '12345678900', 'telefone': '+55 43 9 99999999', 'endereço': 'Rua dos bobos nº 0'}
pessoa2 = {'nome': 'Maria', 'cpf': '22345678900', 'telefone': '+55 44 9 99999999', 'endereço': 'Rua dos bobos nº 2'}

lista_pessoa = [pessoa1, pessoa2]

'''
A partir do exercício anterior crie uma busca onde o usuário possa procurar uma pessoa por nome, cpf, telefone ou endereço.
'''


def buscar_pessoa(lista, dado):
    for i in lista:
        if dado in i.values():
            return i


print(buscar_pessoa(lista_pessoa, 'João'))
