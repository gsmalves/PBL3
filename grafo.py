# encoding: utf-8
# A linha anterior permite usar acentos no nosso programa.

def gerar_caminhos(grafo, caminho, final):
    """Enumera todos os caminhos no grafo `grafo` iniciados por `caminho` e que terminam no vértice `final`."""

    # Se o caminho de fato atingiu o vértice final, não há o que fazer.
    if caminho[-1] == final:
        yield caminho
        return

    # Procuramos todos os vértices para os quais podemos avançar…
    for vizinho in G[caminho[-1]]:
        # …mas não podemos visitar um vértice que já está no caminho.
        if vizinho in caminho:
            continue
        # Se você estiver usando python3, você pode substituir o for
        # pela linha "yield from gerar_caminhos(grafo, caminho + [vizinho], final)"
        for caminho_maior in gerar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior
# Basicamente o yield cria um generator com base no que retornaria de uma função
# Devemos utilizar o yield ou o generator quando há uma lista muito grande que 
# queremos lidar, para não termos que salvar esta na memória



# Exemplo de uso
G = {'Salvador': ['Belo Horizonte', 'Aracaju'], 'Belo Horizonte': ['Salvador', 'Aracaju', 'São Paulo'], 'Aracaju': ['Salvador', 'Belo Horizonte', 'São Paulo'], 'São Paulo': ['Belo Horizonte', 'Aracaju']}

# origem = input("Digite a cidade de origem:")
# destino= input("Cidade de destino:")
for caminho in gerar_caminhos(G, ['Salvador'], 'São Paulo'):
    print (caminho)