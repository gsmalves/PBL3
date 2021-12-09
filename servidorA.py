from EmpresaA import EmpresaA
from flask import Flask, jsonify, render_template, redirect, url_for, session, request
import json

app = Flask(__name__)
    

@app.route('/empresaA/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        passw = request.form['password']
        return redirect(url_for('raiz'))
            

@app.route('/empresaA', methods=['GET', 'POST'])
def raiz():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        origem = request.form['origem']
        destino = request.form['destino']
        ret = mostrarRotasA(origem, destino)
        print(ret)
        return render_template('search.html', value = ret, response=200)

@app.route('/empresaA/<string:passagem>', methods=['POST'])
def compra(passagem: str):
    print(passagem)
    comprar(passagem)


def mostrarRotasA(origem, destino)->dict:
    empresaA = EmpresaA()
    return json.dumps(empresaA.buscarRotas(origem, destino), ensure_ascii=False)

def comprar(passagem):
    empresaA = EmpresaA()
    ret = empresaA.fazerCompra_bilhete(passagem, "Porto Alegre")
    if ret == True:
        return("Compra Realizada")
    else:
        return("Não foi possível relizar a compra")

# port = int(os.environ.get("PORT", 5000))
app.run(debug=True ,host='localhost', port=5000)