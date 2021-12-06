from EmpresaB import EmpresaB
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/empresaB/', methods=['GET'])
def raiz():
    mostrarRotasB()
    return jsonify({'status': 'Sucess'}), 200

def mostrarRotasB():
    empresaB = EmpresaB()
    
    print('Servidor B conectado!')
    cont = 0
    list = empresaB.buscarRotas('Salvador', 'Porto Alegre')
    # for x in list:
    #     print(str(cont) +" - "+ str(x))
    #     cont = cont + 1
    passagem = input("Digite a rota escolhida:")
    ret = empresaB.fazerCompra_bilhete(list[int(passagem)], "Porto Alegre")
    if ret == True:
            print("Compra Realizada")
    else:
        print("Não foi possível relizar a compra")
    mostrarRotasB()

#port = int(os.environ.get("PORT", 5001))
app.run(debug=True ,host='localhost', port=5001)