from EmpresaA import EmpresaA
   
from flask import Flask, jsonify, json
import os

app = Flask(__name__)

@app.route('/empresaA/', methods=['GET'])
def raiz():
    ret = mostrarRotasA()
    return jsonify(ret), 200

@app.route('/empresaA/', methods=['POST'])
def compra(passagem):
    comprar(passagem)


def mostrarRotasA()->dict:
    empresaA = EmpresaA()
    return json.dumps(empresaA.buscarRotas('Salvador', 'Porto Alegre'), ensure_ascii=False)

def comprar(passagem):
    empresaA = EmpresaA()
    ret = empresaA.fazerCompra_bilhete(list[int(passagem)], "Porto Alegre")
    if ret == True:
        return("Compra Realizada")
    else:
        return("Não foi possível relizar a compra")

# port = int(os.environ.get("PORT", 5000))
app.run(debug=True ,host='localhost', port=5000)