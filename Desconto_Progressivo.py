# Questão 1

# Declaração de variáveis
valor_produto = 0
qtd_produto = 0
qtd_produto = int(qtd_produto)
vlr_produto = float(valor_produto)
com_desconto = 0
sem_desconto = 0
soma_vlr_qtd = 0

print('Bem vindo a Loja do Leonardo Argenta')  # Mensagem de boas vindas
# Solicitação do valor do produto
vlr_produto = float(input("Informe o valor do produto escolhido:\n"))
# Solicitação da quantidade do produto
qtd_produto = int(input('Informe a quantidade do produto: \n'))
soma_vlr_qtd = vlr_produto * qtd_produto  # Cálculo do valor total da compra
if soma_vlr_qtd < 2500:  # Sem desconto aplicado
    print('Desconto não aplicado')
    print('Valor total da compra: R$', soma_vlr_qtd)
elif soma_vlr_qtd >= 2500 and soma_vlr_qtd < 6000:  # 4% de desconto aplicado
    desconto = soma_vlr_qtd * 0.04
    print('Valor SEM desconto: R$', soma_vlr_qtd)
    print('Valor COM desconto: R$', soma_vlr_qtd - desconto)
elif soma_vlr_qtd >= 6000 and soma_vlr_qtd < 10000:  # 7% de desconto aplicado
    desconto = soma_vlr_qtd * 0.07
    print('Valor SEM desconto: R$', soma_vlr_qtd)
    print('Valor COM desconto: R$', soma_vlr_qtd - desconto)
else:
    desconto = soma_vlr_qtd * 0.11  # 11% de desconto aplicado
    print('Valor total SEM desconto: R$', soma_vlr_qtd)
    print('Valor total COM desconto: R$', soma_vlr_qtd - desconto)
