from Empresa import EmpresaA



def mostrarRotas():
    empresaA = EmpresaA()
    
    print('Servidor A conectado!')
    cont = 0
    list = empresaA.buscarRotas('Salvador', 'Porto Alegre')
    for x in list:
        print(str(cont) +" - "+ str(x))
        cont = cont + 1
    passagem = input("Digite a rota escolhida:")
    ret = empresaA.fazerCompra_bilhete(list[int(passagem)], "Porto Alegre")
    if ret == True:
            print("Compra Realizada")
    else:
        print("Não foi possível relizar a compra")

    mostrarRotas()

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