import dfs
from models.grafo import G

rotas = []

origem = input("Digite a cidade de origem:")
destino = input("Cidade de destino:")
cont = 0
for caminho in dfs.buscarRotas(G, origem, destino):
    rotas.append(caminho)
    print('{} {}'.format(cont, caminho))
    cont+=1
escolha = input("Trecho escolhido:")

