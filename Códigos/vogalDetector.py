    # Aspas Trilas é usada para textos longos de multiplas linhas. 
    #  for - uma estrutura de reptição ligado ao (enumerate) que é utilizado para obter o indice do texto (i) e dos caracteres (letra).
    # if else - verifica se há um dos dois caracteres solicitados no programa e imprime a posição e a vogal.

texto = """A inserção de comentários no código do programa é uma 
prática normal. Em função disso, toda linguagem de 
programação tem alguma maneira de permitir que 
comentários sejam inseridos nos programas. O objetivo 
é adicionar descrições em partes do código, seja 
para documentá-lo ou para adicionar uma descrição 
do algoritmo implementado (BANIN, p. 45, 2018)." """

for i, letra in enumerate(texto):
    if letra == 'ó' or letra == 'ã':
        print(f"A letra '{letra}' encontrada, na posição {i}")
    
