# Defina o nome do arquivo VEP
nome_arquivo = 'vep.txt'

# Inicialize um conjunto para armazenar os genes únicos
genes_unicos = set()

# Abra o arquivo VEP e leia linha por linha
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        if linha.startswith('#'):
            continue  # Pular cabeçalhos se houver
        
        # Dividir a linha pelos espaços em branco para obter as colunas
        colunas = linha.strip().split()
        
        # Acessar o gene na coluna 7 (índice 6 em Python, pois a indexação começa em 0)
        gene = colunas[6]
        
        # Adicionar o gene ao conjunto de genes únicos
        genes_unicos.add(gene)

# Contar o número de genes únicos
quantidade_genes = len(genes_unicos)

# Imprimir o resultado
print(f'Número de genes únicos no arquivo VEP: {quantidade_genes}')
