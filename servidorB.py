from EmpresaB import EmpresaB
import requests
from flask import Flask, jsonify, render_template, redirect, url_for, session, request
import json


app = Flask(__name__)

@app.route('/empresaB/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        passw = request.form['password']
        return redirect(url_for('raiz'))
            

@app.route('/empresaB', methods=['GET', 'POST'])
def raiz():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        origem = request.form['origem']
        destino = request.form['destino']
        ret = mostrarRotasB(origem, destino)
        resp = ret
        for x in ret:
            rota = ''
            for i in x['rota']:
                rota = rota +"->"+ i
            x['rota'] = rota
        return render_template('search.html', value = ret, v = resp)

@app.route('/comprar', methods=['POST'])
def compra():
    p = request.form['passagem']
    p = eval(p)
    resp = False
    for i in p['info']:
        if i[0] == 'A':
            resp = requests.post(url=f'http://localhost:5000/reserva/empresaA/{i[1:5]}').json()
        elif i[0] == 'B':
            resp = requests.post(url=f'http://localhost:5000/reserva/empresaB/{i[1:5]}').json()
        elif i[0] == 'C':
            resp = requests.post(url=f'http://localhost:5000/reserva/empresaC/{i[1:5]}').json()
    if resp == 200:
        for i in p['info']:
            requests.post(url=f'http://localhost:5000/comprar/empresaA/{i[1:5]}').json()
            requests.post(url=f'http://localhost:5000/comprar/empresaB/{i[1:5]}').json()
            requests.post(url=f'http://localhost:5000/comprar/empresaC/{i[1:5]}').json()
    else:
        print("Nao tem passagem")


    return render_template('home.html')


@app.route('/reserva/empresaB/<string:trecho>', methods=['POST'])
def reservar(trecho: str):
    if reserva(trecho) == True:
        return "200"
    else:
        return "404"
     

@app.route('/comprar/empresaB/<string:trecho>', methods=['POST'])
def comprar(trecho: str):
    comprar(trecho)
    return "200"

def mostrarRotasB(origem, destino)->dict:
    empresaB = EmpresaB()
    return empresaB.buscarRotas(origem, destino)

def reserva(passagem):
    empresaB = EmpresaB()
    ret = empresaB.procura_bilhete(passagem)
    return ret

def comprar(passagem):
    empresaB = EmpresaB()
    empresaB.compra_bilhete(passagem)

# port = int(os.environ.get("PORT", 5000))
app.run(debug=True ,host='localhost', port=5000)