from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Corpo.html')

@app.route('/portugês')
def portugues():
    return render_template('primeiro.html')

@app.route('/matemática')
def matematica():
    return render_template('segundo.html')

@app.route('/ciência')
def ciência():
    return render_template('terceiro.html')

@app.route('/geográfia')
def geografia():
    return render_template('quarto.html')

if __name__ == '__main__':
    app.run(debug=True)