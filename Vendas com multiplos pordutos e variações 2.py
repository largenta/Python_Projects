import pandas as pd  # Importação da biblioteca pandas

print('Bem vindo a gráfica de Leonardo Argenta')  # Mensagem de boas vindas

# Criação do cardápio de serviços
servicos = pd.DataFrame({'Serviço': ['Digitação', 'Iconografia', 'Impressão PB', 'Fotocópia'],
                         'Código': ['dig', 'ico', 'ipb', 'fot'],
                         'Preço por página': [1.10, 1.00, 0.40, 0.20]})

# Criação do cardápio de descontos
descontos = pd.DataFrame({'Intervalo de páginas': ['< 20', '20 - 199', '200 - 1999', '2000 - 19999', '>= 20000'],
                          'Desconto': ['0%', '15%', '20%', '25%', 'Não aceito']})

# Criação do cardápio de serviços extras
extras = pd.DataFrame({'Serviço Extra': ['Nenhum', 'Encadernação simples', 'Encadernação com capa dura'],
                       'Código': ['0', '1', '2'],
                       'Preço': [0.00, 15.00, 40.00]})

# Exibir tabelas
print("Cardápio de Serviços:")
print(servicos.to_string(index=False))
print("\nTabela de Descontos:")
print(descontos.to_string(index=False))
print("\nServiços Extras:")
print(extras.to_string(index=False))


def escolha_servico():
    opcoes = {'dig': 1.10, 'ico': 1.00, 'ipb': 0.40,
              'fot': 0.20}  # Criação do dicionário de serviços
    while True:
        # Input do serviço
        servicos = input(
            'Escolha o serviço desejado (dig, ico, ipb, fot): \n').lower()
        if servicos not in opcoes:
            print(
                'Serviço inválido, tente novamente\n')
            continue
        else:
            return opcoes[servicos]  # Retorno do valor do serviço


def num_paginas():
    while True:
        try:
            # Input do número de páginas
            num_pag = int(input('Digite o número de páginas: \n'))
            if num_pag >= 20000:
                print(
                    'Não aceitamos tantas páginas de uma vez, faça um pedido com menos de 20000 páginas:\n')
                continue
            elif num_pag >= 2000 and num_pag < 20000:
                return num_pag * 0.75  # Retorno do valor total com 25% de desconto
            elif num_pag >= 200 and num_pag < 2000:
                return num_pag * 0.80  # Retorno do valor total com 20% de desconto
            elif num_pag >= 20 and num_pag < 200:
                return num_pag * 0.85  # Retorno do valor total com 15% de desconto
            else:
                return num_pag  # Retorno do valor total sem desconto
        except ValueError:
            # Mensagem de erro
            print('Número de páginas inválido, tente novamente')


def serv_extra():
    # Criação do dicionário de serviços extras
    extras = {'1': 15.00, '2': 20.00, '0': 0.00}
    while True:
        # Input do serviço extra
        serv_extra = input(
            'Escolha um serviço extra (0: Nenhum, 1: Encadernação simples ou 2: Encadernação com capa dura):\n')
        if serv_extra not in extras:
            print('Serviço extra inválido, tente novamente\n')
            continue
        else:
            return extras[serv_extra]


valor_servico = escolha_servico()
quantidade_paginas = num_paginas()
valor_extra = serv_extra()

total = (valor_servico * quantidade_paginas) + \
    valor_extra  # Cálculo do valor total

# Mensagem do valor total da compra
print('O valor total da sua compra é R$', total)
