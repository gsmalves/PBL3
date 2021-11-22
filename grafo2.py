G =  {'Salvador': ['Belo Horizonte', 'Aracaju'], 
'Belo Horizonte': ['Salvador', 'Aracaju', 'São Paulo'],
 'Aracaju': ['Salvador', 'Belo Horizonte', 'São Paulo'], 
 'São Paulo': ['Belo Horizonte', 'Aracaju']}


def dfs_caminhos(grafo, inicio, fim):
    pilha = [(inicio, [inicio])]
    while pilha:
        vertice, caminho = pilha.pop()
        for proximo in set(grafo[vertice]) - set(caminho):
            if proximo == fim:
                yield caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))

# caminhos = list(dfs_caminhos(G, 'Salvador', 'São Paulo'))
# print(caminhos)
origem = input("Digite a cidade de origem:")
destino= input("Cidade de destino:")
for caminho in dfs_caminhos(G, origem, destino):
    print (caminho)
