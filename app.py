# app.py
from flask import Flask, render_template, request, jsonify
import config
import motores

app = Flask(__name__)

# app.py (Fragmento de la ruta Home)
@app.route('/')
def home():
    #lista de recetas al HTML usando el motor Jinja2 de Flask
    return render_template('index.html', lista_cocteles=config.RECETAS.keys())

@app.route('/servir', methods=['POST'])
def servir():
    data = request.get_json()
    coctel_solicitado = data.get('coctel')
    token_recibido = data.get('token')

    # Validación de seguridad 
    if token_recibido != config.TOKEN_SECRETO:
        return jsonify({"mensaje": "ACCESO DENEGADO"}), 401

    # Verificacion de receta 90
    
    if coctel_solicitado in config.RECETAS:
        receta = config.RECETAS[coctel_solicitado]
        
        # Le ordenamos al módulo de motores que empiece a servir en paralelo
        motores.dispensar_coctel(receta)
        
        return jsonify({"mensaje": f"Sirviendo {coctel_solicitado.upper()}..."})
    
    return jsonify({"mensaje": "Coctel no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)