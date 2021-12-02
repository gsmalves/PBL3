from Empresa import EmpresaA


def fazerCompra(self):

    try:
        print('Servidor A conectado!')
        print(EmpresaA.buscarRotas('Salvador', 'Porto Alegre'))
    except:
        print('Erro ao conectar ao servidor A')

    try:
        print('Servidor B conectado!')
        #print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
    except:
        print('Erro ao conectar ao servidor B')

    try:
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
    empresaA = EmpresaA()
    try:
        print('Servidor A conectado!')
        print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
    except:
        print('Erro ao conectar ao servidor A')

    try:
        print('Servidor B conectado!')
        # print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
    except:
        print('Erro ao conectar ao servidor B')

    try:
        print('Servidor C conectado!')
        # print(empresaA.buscarRotas('Salvador', 'Porto Alegre'))
    except:
        print('Erro ao conectar ao servidor C')


    


if __name__ == "__main__":
    mostrarRotas()