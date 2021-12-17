'''
 * Componente Curricular: Módulo Integrado de Concorrência e Conectividade
 * Autor: Gustavo dos Santos Menezes Alves e Esther de Santana Araújo
 * Data: 4/11/2021
 *
 * Declaro que este código foi elaborado por nós de forma colaborativa e
 * não contém nenhum trecho de código de outro colega ou de outro autor,
 * tais como provindos de livros e apostilas, e páginas ou documentos
 * eletrônicos da Internet. Qualquer trecho de código de outra autoria que
 * uma citação para o  não a minha está destacado com  autor e a fonte do
 * código, e estou ciente que estes trechos não serão considerados para fins
 * de avaliação. Alguns trechos do código podem coincidir com de outros
 * colegas pois estes foram discutidos em sessões tutorias.
 '''
 
from EmpresaC import EmpresaC
import requests, time, json
from bully import Processos, processos
from flask import Flask, render_template, redirect, url_for, request, flash, Markup
import  os
from dotenv import load_dotenv
import parse
import threading


load_dotenv()

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
host=os.getenv("prod")
clientes = []
processes = []
id_coordenador = 1


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        passw = request.form['password']
        return redirect(url_for('raiz', user=name))

@app.route('/updateCoordenador/<int:id>', methods=['PUT'])
def updateCoordenador(id):
    global id_coordenador
    id_coordenador = id


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

#Rota que reserva as passagens (verifica se estao disponíveis) e realiza a compra
@app.route('/reservar', methods=['POST'])
def compra():
    p = request.form['passagem']
    p = eval(p)
    for i in p['info']:
            if i[0] == 'A':
                resp = requests.post(url=f'{os.getenv("airlinesA")}/reserva/empresaA/{i[1:5]}').json()
                if resp == 404:
                    break
            elif i[0] == 'B':
                resp = requests.post(url=f'{os.getenv("airlinesB")}/reserva/empresaB/{i[1:5]}').json()
                if resp == 404:
                    break
            elif i[0] == 'C':
                resp = requests.post(url=f'{os.getenv("airlinesC")}/reserva/empresaC/{i[1:5]}').json()
                if resp == 404:
                    break
    if resp == 404:
        return render_template('confirmacao.html', conf=False, passagem=p)
    else:
        for i in p['info']:
            requests.post(url=f'{os.getenv("airlinesA")}/comprar/empresaA/{i[0:5]}').json()
            requests.post(url=f'{os.getenv("airlinesB")}/comprar/empresaB/{i[0:5]}').json()
            requests.post(url=f'{os.getenv("airlinesC")}/comprar/empresaC/{i[0:5]}').json()
        return render_template('confirmacao.html', conf=True, passagem=p)
    
    
@app.route('/reserva/empresaC/<string:trecho>', methods=['POST'])
def reservar(trecho: str):
    if reserva(trecho) == True:
        return  json.dumps("200")
    else:
        return json.dumps("404")


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

def gerencia_reservas():
    for p in clientes:
        for i in p['info']:
            if i[0] == 'A':
                resp = requests.post(url=f'{os.getenv("airlinesA")}/reserva/empresaA/{i[1:5]}').json()
                if resp == 404:
                    break
            elif i[0] == 'B':
                resp = requests.post(url=f'{os.getenv("airlinesB")}/reserva/empresaB/{i[1:5]}').json()
                if resp == 404:
                    break
            elif i[0] == 'C':
                resp = requests.post(url=f'{os.getenv("airlinesC")}/reserva/empresaC/{i[1:5]}').json()
                if resp == 404:
                    break
        if resp == 404:
            return render_template('confirmacao.html', conf=False, passagem=p)
        else:
            for i in p['info']:
                requests.post(url=f'{os.getenv("airlinesA")}/comprar/empresaA/{i[0:5]}').json()
                requests.post(url=f'{os.getenv("airlinesB")}/comprar/empresaB/{i[0:5]}').json()
                requests.post(url=f'{os.getenv("airlinesC")}/comprar/empresaC/{i[0:5]}').json()
            Processos.kill_process_by_id(resp[1])
            return render_template('confirmacao.html', conf=True, passagem=p)


class ThreadEleicao(str):
    coordenador = (str)

    def run(self):
        while 1:
            time.sleep(1)
            self.coordenador.emit()

def election(process):
    id_coordenador = process.eleicao()
    if id_coordenador == 1:
        gerencia_reservas()


if __name__ == '__main__':
    # conf_file = open("file.config","r")
    # input = conf_file.readlines()
    # n = int(input[0])
    # for i in range(1,n+1):
    #     line = parse.parse('{} {}', input[i])
    #     processes.append({'url': line[0], 'id': line[1]})
    # processC = Processos(1, 1)
    # thread_start = ThreadEleicao()
    # thread_start.coordenador.connect(election(processC))
    # thread_start.start()
    app.run(debug=True ,host=host, port=port)
