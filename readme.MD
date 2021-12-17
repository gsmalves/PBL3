# PBL3-Redes - Malha aérea compartilhada


## Para executar a aplicação de modo remoto
Como as três companhias aéreas estão hospedadas no Heroku, basta apenas acessar o link de uma das três:
https://airlines-a.herokuapp.com/
https://airlines-b.herokuapp.com
https://airlines-c.herokuapp.com/


## Para executar a aplicação localmente
## Pré-requisitos

Para rodar a aplicação web, você vai precisar ter instalado:
[Python 3.5 ou superior](https://www.python.org/downloads/) - 


```bash
# Instale as dependências
$ pip install -r requirements.txt
```

### Alterar o host
É necessário alterar a variável host=os.getenv("prod") presente no arquivo main.py de cada empresa, no lugar de "prod", inserir "dev". Assim o arquivo rodará no localhost, porta 5000.

### Executar a main estando na pasta da empresa que desejar
$ python main.py
