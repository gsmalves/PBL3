G = {
    'Belém': [{'cidade': 'Salvador', 'tempo': 4, 'empresa': 'C', 'numero': 1992, 'bilhetes': 10},
              {'cidade': 'Porto Alegre', 'tempo': 3,
               'empresa': 'B', 'numero': 1993, 'bilhetes': 10},
              {'cidade': 'Brasília', 'tempo': 2, 'empresa': 'A', 'numero': 1993, 'bilhetes': 10}],
    'São Paulo': [{'cidade': 'Belém', 'tempo': 5, 'empresa': 'B', 'numero': 1979, 'bilhetes': 10},
                  {'cidade': 'Porto Alegre', 'tempo': 3,
                   'empresa': 'B', 'numero': 1004, 'bilhetes': 10},
                  {'cidade': 'Rio de Janeiro', 'tempo': 1, 'empresa': 'C', 'numero': 1985, 'bilhetes': 10}],

    'Porto Alegre': [{'cidade': 'Salvador', 'tempo': 3, 'empresa': 'A', 'numero': 1994, 'bilhetes': 10},
                     {'cidade': 'Belém', 'tempo': 6, 'empresa': 'C',
                      'numero': 1995, 'bilhetes': 10},
                     {'cidade': 'Brasília', 'tempo': 1, 'empresa': 'A', 'numero': 1996, 'bilhetes': 10}],
    'Brasília': [{'cidade': 'Belém', 'tempo': 4, 'empresa': 'A', 'numero': 1997, 'bilhetes': 10},
                 {'cidade': 'Porto Alegre', 'tempo': 3,
                  'empresa': 'B', 'numero': 1998, 'bilhetes': 10},
                 {'cidade': 'Recife', 'tempo': 4, 'empresa': 'A', 'numero': 1974, 'bilhetes': 10}],

    'Recife': [{'cidade': 'Salvador', 'tempo': 2, 'empresa': 'C', 'numero': 1999, 'bilhetes': 10},
               {'cidade': 'Rio de Janeiro', 'tempo': 4, 'empresa': 'C', 'numero': 1980, 'bilhetes': 10}],
    'Salvador': [{'cidade': 'Belém', 'tempo': 1, 'empresa': 'A', 'numero': 1990, 'bilhetes': 10},
                 {'cidade': 'Porto Alegre', 'tempo': 2, 'empresa': 'B', 'numero': 1991, 'bilhetes': 10}],
    'Rio de Janeiro': [{'cidade': 'São Paulo', 'tempo': 1, 'empresa': 'C', 'numero': 1986, 'bilhetes': 10},
                       {'cidade': 'Recife', 'tempo': 4, 'empresa': 'A', 'numero': 1981, 'bilhetes': 10}]}


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
