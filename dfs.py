from models.grafo import G

def buscarRotas(grafo, inicio, fim):
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
