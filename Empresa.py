class Voo:
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