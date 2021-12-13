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

    def aux_3(self, inicio, fim):
        for x in G[inicio]:
            if x['cidade'] == fim:
                x['bilhetes'] = x['bilhetes'] - 1
    
    def procura_bilhete(self, numero)->bool:
        for x in G:
            for i in G[x]:
                if i['numero'] == int(numero):
                    if i['bilhetes'] > 0:
                        return True
        return False
    
    def compra_bilhete(self, numero):
        for x in G:
            for i in G[x]:
                if i['numero'] == int(numero):
                    i['bilhetes'] -= 1 
    
    def fazerCompra_bilhete(self, rota, fim):
        try:
            self.fazerCompra_bilhete2(rota, fim)
        except:
            print('Erro ao conectar ao servidor B')
        if len(self.busca_bilhete_2(rota)) == 0:
            for x in range(len(rota)):
                if rota[x] == fim:
                    break

                self.aux_3(rota[x], rota[x + 1])


            for x in self.buscarEmp(rota, fim):
                if x == 'A':
                    relogio = self.relogio_lamport()

            aux = {'rota': rota,'relogio': relogio}


            self.compradores.append(aux)
            print(self.compradores)

            return True

        return False
    
    def fazerCompra_bilhete2(self, rota, fim):
        print(rota)
        if len(self.busca_bilhete_2(rota)) == 0:
            for x in range(len(rota)):
                if rota[x] == fim:
                    break
                self.aux_3(rota[x], rota[x + 1])

            for x in self.buscarEmp(rota, fim):
                if x == 'A':
                    relogio = self.relogio_lamport()
    
    def busca_bilhete_2(self, rota):
        aux = []
        for x in range(len(rota)):
                if type(rota[x]) != int:
                    if len(rota[x].split('|')) == 2 and int(rota[x].split('|')[1]) == 0:
                        aux.append(rota[x])

        return aux
    
    def buscarEmp(self, caminhos, fim):
        listEmp = []

        for x in range(len(caminhos) - 2):
            i = self.auxEmp(caminhos[x], caminhos[x + 1])
            listEmp.append(i)
            if caminhos[x] == fim:
                break

        return listEmp
    
    def auxEmp(self, ini, fim):
        tempo = ''
        for x in G[ini]:
            if x['cidade'] == fim:
                tempo = x['empresa']

        return tempo

    def buscarRotas(self, origem, destino) -> list:
        caminhos = list(dfs.dfs_caminhos(G, origem, destino))
        tempo = 0
        rotas = []
        for x in caminhos:
            tempo = self.tempoTotal(x)
            preco = self.somaPreco(x)
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
        for x in range(len(caminhos) - 2):
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

    def remove(self, caminhos):
        aux = self.busca_bilhete(caminhos)
        for x in aux:
            caminhos.remove(x)
        time.sleep(0.2)
        return caminhos

    def busca_bilhete(self, caminhos):

        aux = []
        for x in range(len(caminhos)):
            for y in range(len(caminhos[x])):
                    if type(caminhos[x][y]) != int:
                         if len(caminhos[x][y].split('|')) == 2 and int(caminhos[x][y].split('|')[1]) == 0:
                            aux.append(caminhos[x])

        return aux
