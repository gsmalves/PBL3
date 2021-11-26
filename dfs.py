from models.grafo import G

def dfs_caminhos(grafo, inicio, fim):
    # Insere o primeiro nó na pilha
    pilha = [(inicio, [inicio])]
    while pilha:
        vertice, caminho = pilha.pop()
        for proximo in set(aux(grafo[vertice])) - set(caminho):
            if proximo == fim:
                yield caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))


def aux(list):
    retorno = []
    for x in list:
        retorno.append(x['cidade'])
    return retorno


origem = input("Digite a cidade de origem:")
destino = input("Cidade de destino:")
for caminho in dfs_caminhos(G, origem, destino):
    print(caminho)
