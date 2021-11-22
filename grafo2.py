G =  {'Salvador': ['Belo Horizonte', 'Aracaju'], 'Belo Horizonte': ['Salvador', 'Aracaju', 'São Paulo'], 'Aracaju': ['Salvador', 'Belo Horizonte', 'São Paulo'], 'São Paulo': ['Belo Horizonte', 'Aracaju']}


def dfs_caminhos(grafo, inicio, fim):
    #Insere o primeiro nó na pilha
    pilha = [(inicio, [inicio])]
    while pilha:
        vertice, caminho = pilha.pop()
        #Passa pelos vértices não visitados
        for proximo in set(grafo[vertice]) - set(caminho):
            #Chegando no destino, retorna os caminhos
            if proximo == fim:
                yield caminho + [proximo]
            else:
                #Empilha os vértices não visitados
                pilha.append((proximo, caminho + [proximo]))

# caminhos = list(dfs_caminhos(G, 'Salvador', 'São Paulo'))
# print(caminhos)
origem = input("Digite a cidade de origem:")
destino= input("Cidade de destino:")
for caminho in dfs_caminhos(G, origem, destino):
    print (caminho)
