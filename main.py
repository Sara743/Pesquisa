# lista de 15 nomes
nomes = [ 'Alex','Eduardo', 'Maria','Mariana', 'João', 'José', 'Joana', 'Fernada', 'Fulano', 'Cicrano', 'Beltrano', 'Connor', 'Corona', 'Cecilia', 'Alexandre']

# usuario informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado:'). capitalize()

# retorne o indice a ser pesquisado
#indice = nomes.index(nome)

# verifica se o nome está na lista ou não
#if nome in nomes:
    #print(f'Nome encontado: {nome} no indice {indice}.')
#else:
   # print(f'{nome} não encontado na lista.')

# verifica se o nome está na lista ou não
try:
    # rettorne o indice do nome pesquisado
    indice = nomes.index(nome)
    print(f'Nome encontado: {nome} no indice {indice}.')
except:
    print(f'{nome} não encontado na lista.')

