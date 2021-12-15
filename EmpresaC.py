import dfs, time
from models.grafo import G

rotas = []

class EmpresaC:
    def __init__(self):
        self.processos = 3
        self.relogio = [[0] for self.i in range(self.processos)]
        self.log = []

        self.numerovoo = ''
        self.tempo = ''
        self.origem = ''
        self.destino = ''
        self.compradores = []

    def evento(self, p_envia, p_recebe):

            if p_envia == p_recebe:
                self.relogio[p_envia].append(self.relogio[p_envia][-1] + 1)

            else:
                self.relogio[p_envia].append(self.relogio[p_envia][-1] + 1)

                if self.relogio[p_envia][-1] > self.relogio[p_recebe][-1]:
                    self.relogio[p_recebe].append(self.relogio[p_envia][-1] + 1)

                else:
                    self.relogio[p_recebe].append(self.relogio[p_recebe][-1] + 1)

            self.log.append("[%s]---->" % p_envia)
            self.log.append("[%s]" % p_recebe)

            return self.relogio[p_envia]


    def relogio_lamport(self):
        aux = [0, 0, 0]

        eventoEmpresaA = self.evento(0, 0)
        aux[0] = eventoEmpresaA[len(eventoEmpresaA) - 1]
        eventoEmpresaB = self.evento(0, 1)
        aux[1] = eventoEmpresaB[len(eventoEmpresaB) - 1]
        eventoEmpresaC = self.evento(0, 2)
        aux[2] = eventoEmpresaC[len(eventoEmpresaC) - 1]

        return aux

    
    def procura_bilhete(self, numero)->bool:
        for x in G:
            for i in G[x]:
                if i['numero'] == int(numero):
                    return True
        return False
    
    def compra_bilhete(self, numero):
        for x in G:
            for i in G[x]:
                if i['numero'] == int(numero[1:5]) and i['empresa']==numero[0]:
                    i['bilhetes'] -= 1
                    if i['bilhetes'] == 0:   
                        G[x].remove(i)
    


    def buscarRotas(self, origem, destino) -> list:
        caminhos = list(dfs.dfs_caminhos(G, origem, destino))
        tempo = 0
        rotas = []
        preco = 0
        for x in caminhos:
            tempo = self.tempoTotal(x)
            preco = self.precoTotal(x)
            info = self.add_infos(x)
            j = self.create_json(x, tempo,preco, info)
            rotas.append(j)
        return rotas
    
    def create_json(self, rota, tempo,preco, info) -> dict:
        return {
            'rota': rota,
            'tempo': tempo,
            'preco': preco,
            'info': info
        }
    
    def tempoTotal(self, caminhos):
        i = 0
        for x in range(len(caminhos) - 1):
            i = i + self.soma(caminhos[x], caminhos[x + 1])

        return i

    def add_infos(self, caminhos):
        info = []
        for x in range(len(caminhos) - 1):
            i = self.aux_2(caminhos[x], caminhos[x + 1])
            info.append(i)

        return info
    
    def aux_2(self, ini, fim):
        tempo = ''
        for x in G[ini]:
            if x['cidade'] == fim:
                tempo = x['empresa'] + str(x['numero']) + '|' + str(x['bilhetes'])

        return tempo
    
    def soma(self, ini, fim):
        tempo = 0
        for x in G[ini]:
            if x['cidade'] == fim:
                tempo = x['tempo']

        return tempo

        
    def somaPreco(self, ini, fim):
        preco = 0
        for x in G[ini]:
            if x['cidade'] == fim:
                preco = x['preco']

        return preco

    def precoTotal(self, caminhos):
        temp = 0
        for x in range(len(caminhos) - 1):
            temp = temp + self.somaPreco(caminhos[x], caminhos[x + 1])

        return temp

