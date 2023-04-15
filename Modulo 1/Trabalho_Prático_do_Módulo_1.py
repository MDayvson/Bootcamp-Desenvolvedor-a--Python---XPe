# 1

# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)

# 2

inicio = 100
fim = 500
for numero in range(inicio,fim):
    if numero % 2 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print(numero)

# 3

divisor = 3

for numero in range (1000):
    if numero % divisor == 0:
        print(numero)
    
# 4

# variaveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

nome = nome.upper()
cidade = cidade.upper()

nome = nome.lower()
cidade = cidade.lower()

posição_de_ã_em_nome = nome.find('ã')
posição_de_ã_em_cidade = cidade.find('ã')

tamanho_nome = len(nome)
tamanho_cidade = len(cidade)
tamanho_cpf = len(cpf)

novo_cpf = cpf.replace('.','').replace('-','')
print(novo_cpf)


# 5

numero = '127957'

print(type(int(numero) + 1.0))

soma = 0
for num in numero:
    soma += int(num)
print(soma)
