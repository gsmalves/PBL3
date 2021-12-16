from EmpresaC import EmpresaC
import requests, time, json
from bully import Processos, processos
from flask import Flask, render_template, redirect, url_for, request, flash, Markup
import  os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
host=os.getenv("prod")
id_coordenador = 0
cont = 0


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        passw = request.form['password']
        return redirect(url_for('raiz', user=name))

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')
            

@app.route('/empresaC/<string:user>', methods=['GET'])
def raiz(user):
        return render_template('home.html', usr=user)

@app.route('/empresaC', methods=['POST'])
def search():
    origem = request.form['origem']
    destino = request.form['destino']
    ret = mostrarRotasC(origem, destino)
    resp = ret
    for x in ret:
        rota = ''
        for i in x['rota']:
            rota = rota +"->"+ i
        x['rota'] = rota
    return render_template('search.html', value = ret)


@app.route('/reservar', methods=['POST'])
def compra():
    p = request.form['passagem']
    p = eval(p)
    resp = False
    for i in p['info']:
        if i[0] == 'A':
            resp = requests.post(url=f'{os.getenv("airlinesA")}/reserva/empresaA/{i[1:5]}').json()
            if resp[0] == 404:
                break
        elif i[0] == 'B':
            resp = requests.post(url=f'{os.getenv("airlinesB")}/reserva/empresaB/{i[1:5]}').json()
            if resp[0] == 404:
                break
        elif i[0] == 'C':
            resp = requests.post(url=f'{os.getenv("airlinesC")}/reserva/empresaC/{i[1:5]}').json()
            if resp[0] == 404:
                break
    
    if resp[0] == 404:
        return render_template('confirmacao.html', conf=False, passagem=p)
    else:
        for i in p['info']:
            requests.post(url=f'{os.getenv("airlinesA")}/comprar/empresaA/{i[0:5]}').json()
            requests.post(url=f'{os.getenv("airlinesB")}/comprar/empresaB/{i[0:5]}').json()
            requests.post(url=f'{os.getenv("airlinesC")}/comprar/empresaC/{i[0:5]}').json()
        Processos.kill_process_by_id(resp[1])
        return render_template('confirmacao.html', conf=True, passagem=p)
    
@app.route('/reserva/empresaC/<string:trecho>', methods=['POST'])
def reservar(trecho: str):
    global cont
    process = Processos(id_coordenador, cont)
    processos.append(process)
    cont = cont + 1
    while True:
        t = process.eleicao()
        if t == process.get_id_process():
            break
    if reserva(trecho) == True:
        return  json.dumps(["200", process.get_id_process()])
    else:
        return json.dumps(["404", process.get_id_process()])
     

@app.route('/comprar/empresaC/<string:trecho>', methods=['POST'])
def comprar(trecho: str):
    compra(trecho)
    return "200"

def mostrarRotasC(origem, destino)->dict:
    empresaC = EmpresaC()
    return empresaC.buscarRotas(origem, destino)

def reserva(passagem):
    empresaC = EmpresaC()
    ret = empresaC.procura_bilhete(passagem)
    return ret

def compra(passagem):
    empresaC = EmpresaC()
    empresaC.compra_bilhete(passagem)

if __name__ == '__main__':
    app.run(debug=True ,host=host, port=port)
