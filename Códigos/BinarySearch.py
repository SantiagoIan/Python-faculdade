#seção 2.2 - slide 16 (abordagem prática)
def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
      
        meio = (minimo + maximo) // 2 # Encontra o elemento que divide a lista ao meio
        # Verifica se o valor procurado está a esquerda ou 
        # direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # Se o valor for encontrado para aqui
    return False # Significa que o valor não foi encontrado



import random

lista = random.sample(range(999), 250)
lista=(sorted(lista))
print(lista,'\n')


print(f"\n Buscando o número 501 na lista: {executar_busca_binaria(lista,501)}")
print(f"\n Buscand o número 637 na lista: {executar_busca_binaria(lista,637)}")

p=random.randint(1, 999) # Criando uma variavel para receber um número aleatorio entre 1 a 999.

if executar_busca_binaria(lista, p):
    print(f"\n Número {p} encontrado")
else:
    print(f"\nNúmero {p} não encontrado")
