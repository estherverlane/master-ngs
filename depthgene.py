# script para realizar o calculo de cobertura em extensão de varias regioes de uma vez
import subprocess

# Lista de cromossomos e seus intervalos
values = [
    ("chr17", 14029292, 14069458),
    ("chr17", 13755574, 14069495)
]

# Loop para executar o comando awk para cada conjunto de valores
for value in values:
    pattern, start_range, end_range = value
    # Gerar o comando awk e o nome do arquivo de saída com o sufixo correto
    command = f"awk '$1 == \"{pattern}\" && $2 >= {start_range} && $2 <= {end_range}' <arquivo_depth> > {pattern}-{start_range}-{end_range}_arquivo_depth_sort.txt"
    print(f"Executando: {command}")
    subprocess.run(command, shell=True)
