class Main():
    def fazerCompra(self):

        try:
            nsA = Pyro4.locateNS('172.16.103.10', 5000)
            uriA = nsA.lookup('objA')
            empresaA = Pyro4.Proxy(uriA)
            print('Servidor A conectado!')
            #print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
        except:
            print('Erro ao conectar ao servidor A')

        try:
            nsB = Pyro4.locateNS('172.16.103.11', 5001)
            uriB = nsB.lookup('objB')
            empresaB = Pyro4.Proxy(uriB)
            print('Servidor B conectado!')
            #print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
        except:
            print('Erro ao conectar ao servidor B')

        try:
            nsC = Pyro4.locateNS('172.16.103.12', 5002)
            uriC = nsC.lookup('objC')
            empresaC = Pyro4.Proxy(uriC)
            print('Servidor C conectado!')
            # print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
        except:
            print('Erro ao conectar ao servidor C')


        # if retorno == True:
        #     self.dialogCompraTrue()
        # else:
        #     self.dialogCompraFalse()
        self.mostrarRotas()
    
    def mostrarRotas():

        try:
            nsA = Pyro4.locateNS('172.16.103.10', 5000)
            uriA = nsA.lookup('objA')
            empresaA = Pyro4.Proxy(uriA)
            print('Servidor A conectado!')
            # print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
        except:
            print('Erro ao conectar ao servidor A')

        try:
            nsB = Pyro4.locateNS('172.16.103.11', 5001)
            uriB = nsB.lookup('objB')
            empresaB = Pyro4.Proxy(uriB)
            print('Servidor B conectado!')
            # print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
        except:
            print('Erro ao conectar ao servidor B')

        try:
            nsC = Pyro4.locateNS('172.16.103.12', 5002)
            uriC = nsC.lookup('objC')
            empresaC = Pyro4.Proxy(uriC)
            print('Servidor C conectado!')
            # print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
        except:
            print('Erro ao conectar ao servidor C')


        


if __name__ == "__main__":
    Main()