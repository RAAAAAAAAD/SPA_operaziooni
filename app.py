from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    """Servono per prendere le info dal front end"""
    dati = request.get_json()
    if dati:
        num1 = dati.get('num1')
        num2 = dati.get('num2')
        operazione = dati.get('operazione')
        #elaborazioone delle info
        if operazione == 'addizione':
            risultato = num1 + num2
        elif operazione == 'sotrazione':
            risultato = num1 - num2
        elif operazione == 'moltiplicazione':
            risultato = num1 * num2
        elif operazione == 'divisione':
            risultato = num1 // num2
        #restiturire i dati al front end
        return jsonify(risultato = risultato)
    else:
        return jsonify(risultato = 'mancano i di dati')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)