from flask import Flask, render_template, request, jsonify
from datetime import datetime
# Cria a instância do Flask no App
app = Flask(__name__)

# Banco em memória
banco = []

# Rota de teste
@app.route('/pegar')
def pegar():
    # jsom2 = str(banco)
    return banco


@app.route('/enviar', methods=['POST'])
def enviar():
    numero = int(request.args.get("numero"))
    nome = str(request.args.get("nome"))
    # dados = request.json
    # numero = str(dados.get("numero"))
    # nome = int(dados.get("nome"))
    jsom = jsonify({
        "numero": numero,
        "nome": nome,
        "hora":datetime.now()
    })
    banco.append({
        "numero": numero,
        "nome": nome,
        "hora":datetime.now()
    })
    print(banco)
    return jsom

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)