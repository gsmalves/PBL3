   
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def raiz():
    return jsonify({'status': 'Sucess'}), 200





port = int(os.environ.get("PORT", 5000))
app.run(debug=True ,host='0.0.0.0', port=port)