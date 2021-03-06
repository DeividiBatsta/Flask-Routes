from flask import Flask, render_template

app = Flask(__name__)

lista = [
    ['Refrigerante', 4.50, 'Tomos os refrigerantes de 2lt: Coca-Cola, Sukita, Sprite, Fanta, Schweppes,Guaraná, Soda Antartica, Fors Cola'],
    ['Pizza', 2.50, 'Temos pizza de: Frango, Calabresa, Brocolis, 4 queijos, Presunto e mussarela, Chocolate, Abacaxi, Camarão'],
    ['Suco', 24.90, 'Temos Sucos de: Abacaxi, Morango, Laranja, Limonada, Mamão, Aceróla, Frutas vermelhas, Frutas cítricas'],
    ['Salgados', 5.50, 'Temos estes  tipos de Salgados: Coxinha, Risole, Quibe, empáda, Esfira, Pasteis, Salsicha empanada'],
    ['Lanche', 18.50, 'Temos lanches de: X-tudo, X-file,Super-lombo, Americano, Bauru, X-egg, Bacon-tudo, X-salada']
]

@app.route('/')
def index():

    return render_template(
        'index.html', 
        titulo ='index',
        lista = lista
    )

@app.route('/itens/<int:id>')
def produto(id):
    index = lista[id]
    return render_template('produto.html', item = index )

if __name__ == '__main__':
    app.run()