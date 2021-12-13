from EmpresaC import EmpresaC
import requests
from flask import Flask, render_template, redirect, url_for, request
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        passw = request.form['password']
        return redirect(url_for('raiz'))
            

@app.route('/empresaC', methods=['GET', 'POST'])
def raiz():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        origem = request.form['origem']
        destino = request.form['destino']
        ret = mostrarRotasC(origem, destino)
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
    print(p)
    resp = False
    for i in p['info']:
        if i[0] == 'A':
            resp = requests.post(url=f'{os.getenv("airlinesA")}/reserva/empresaA/{i[1:5]}').json()
        elif i[0] == 'B':
            resp = requests.post(url=f'{os.getenv("airlinesB")}/reserva/empresaB/{i[1:5]}').json()
        elif i[0] == 'C':
            resp = requests.post(url=f'{os.getenv("airlinesC")}/reserva/empresaC/{i[1:5]}').json()
    if resp == 200:
        for i in p['info']:
            requests.post(url=f'{os.getenv("airlinesA")}/comprar/empresaA/{i[1:5]}').json()
            requests.post(url=f'{os.getenv("airlinesB")}/comprar/empresaB/{i[1:5]}').json()
            requests.post(url=f'{os.getenv("airlinesC")}/comprar/empresaC/{i[1:5]}').json()
    else:
        print("Nao tem passagem")


    return render_template('home.html')


@app.route('/reserva/empresaC/<string:trecho>', methods=['POST'])
def reservar(trecho: str):
    if reserva(trecho) == True:
        return "200"
    else:
        return "404"
     

@app.route('/comprar/empresaC/<string:trecho>', methods=['POST'])
def comprar(trecho: str):
    compra_passagem(trecho)
    return "200"

def mostrarRotasC(origem, destino)->dict:
    empresaC = EmpresaC()
    return empresaC.buscarRotas(origem, destino)

def reserva(passagem):
    empresaC = EmpresaC()
    ret = empresaC.procura_bilhete(passagem)
    return ret

def compra_passagem(passagem):
    empresaC = EmpresaC()
    empresaC.compra_bilhete(passagem)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=True ,host=os.environ.get("prod"), port=port)
