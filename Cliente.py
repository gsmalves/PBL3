import requests, json

if __name__ == "__main__":
    empresa = input("Digite a empresa escolhida:")
    if(empresa =="A"):
        cont = 0
        list = requests.get(url=f'http://localhost:5000/empresaA').json()
        for x in list:
            print(str(cont) +" - "+ str(x))
            cont = cont + 1
        passagem = input("Digite a rota escolhida:")
        requests.post(url=f'http://localhost:5000/empresaA/{str(list[int(passagem)])}')

    else:
        requests.get(url=f'http://localhost:5001/empresaB')
