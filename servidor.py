from main import executa_programa
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/resposta', methods=['POST'])
def mostrar_resultados():
    id_botao = request.form.get('id_botao')
    return render_template('index.html',\
                            html_lista_hora=executa_programa()[0],\
                            html_lista_vencedor=executa_programa()[1],\
                            html_lista_perdedor=executa_programa()[2],\
                            html_lista_comportamento_vencedor=executa_programa()[3])


if __name__ =='__main__':
    app.run(host = 'localhost', port = 5000, debug = True)