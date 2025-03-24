# Questão 2
import pandas as pd  # Importação da biblioteca pandas

# Mensagem de boas vindas
print('Bem vindo a Loja de Gelados do Leonardo Argenta')
print('Aqui está o nosso cardápio: ')  # Mensagem do cardápio

cardapio = pd.DataFrame({'Açaí': [11, 16, 20], 'Cupuaçu': [9, 14, 18]}, index=[
                        'Pequeno', 'Médio', 'Grande'])  # Criação do cardápio
print(cardapio)  # Impressão do cardápio

# Declaração de variáveis
vlr_total = 0
vlr_total = float(vlr_total)

while True:  # Loop para repetir o pedido
    # Input do sabor
    sabor = input('Digite AC para açaí e CP para cupuaçu: \n').upper()
    if sabor != 'AC' and sabor != 'CP':  # Condição para sabor inválido
        print('Sabor inválido, tente novamente')
        continue
    # Input do tamanho
    tamanho = input(
        'Digite P para pequeno, M para médio e G para grande: \n').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido, tente novamente')
        continue
    if sabor == 'AC':  # Condição para o sabor de açaí
        if tamanho == 'P':
            preco = 11
        elif tamanho == 'M':
            preco = 16
        else:
            preco = 20
    else:  # Condição para o sabor de cupuaçu
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        else:
            preco = 18

    vlr_total += preco  # Soma do valor total
    # Mensagem do valor total
    print('Seu pedido até agora custa R$', vlr_total)
    # Input para outro pedido
    outro_pedido = input('Deseja fazer outro pedido? (S/N)\n').upper()
    if outro_pedido not in ('N', 'n', 'S', 's'):  # Condição para input inválido
        print('Comando inválido, tente novamente')

    elif outro_pedido in ('N', 'n'):  # Condição para sair do loop
        break
# Mensagem do valor total da compra
print('O valor total da sua compra é R$', vlr_total)
