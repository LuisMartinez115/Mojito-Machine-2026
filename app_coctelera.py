from flask import Flask, render_template_string, request, jsonify
import time

app = Flask(__name__)

TOKEN_SECRETO = "MiCocteleraPrivada2026"

# Simulación de la base de datos de los líquidos y sus "pines virtuales"
MOTORES_VIRTUALES = {
    "ron_blanco": {"pin": 4, "estado": "APAGADO"},
    "vodka": {"pin": 5, "estado": "APAGADO"},
    "jugo_naranja": {"pin": 26, "estado": "APAGADO"},
    "granadina": {"pin": 21, "estado": "APAGADO"}
}

# Diccionario de cocteles predeterminados basados en tu lista (Dosis en segundos de bombeo)
RECETAS = {
    "mojito": {"ron_blanco": 3, "granadina": 1},
    "sex_on_the_beach": {"vodka": 3, "jugo_naranja": 5}
}

# --- DISEÑO VISUAL PARA TU CELULAR (HTML/CSS) ---
HTML_INTERFAZ = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coctelera Smart HMI</title>
    <style>
        body { font-family: Arial, sans-serif; background: #121212; color: white; text-align: center; padding: 20px; }
        h1 { color: #00adb5; }
        .btn-coctel { 
            background: #222831; border: 2px solid #00adb5; color: white; 
            padding: 20px; margin: 15px; width: 80%; max-width: 300px; 
            font-size: 18px; border-radius: 10px; cursor: pointer; transition: 0.3s;
        }
        .btn-coctel:active { background: #00adb5; }
        .token-input { padding: 10px; border-radius: 5px; border: none; margin-bottom: 20px; text-align: center; }
    </style>
</head>
<body>
    <h1>🍸 PANEL DE CONTROL PRIVADO</h1>
    <p>Introduce tu clave de seguridad:</p>
    <input type="password" id="token" class="token-input" value="MiCocteleraPrivada2026"><br>

    <button class="btn-coctel" onclick="servir('mojito')">Preparar Mojito 🍃</button>
    <button class="btn-coctel" onclick="servir('sex_on_the_beach')">Preparar Sex On The Beach 🍊</button>

    <script>
        function servir(nombreCoctel) {
            const token = document.getElementById('token').value;
            
            fetch('/servir', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ coctel: nombreCoctel, token: token })
            })
            .then(res => res.json())
            .then(data => alert(data.mensaje))
            .catch(err => alert("Error de conexión"));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_INTERFAZ)

@app.route('/servir', methods=['POST'])
def servir():
    data = request.get_json()
    coctel_solicitado = data.get('coctel')
    token_recibido = data.get('token')

    # VALIDACIÓN DE SEGURIDAD MÁXIMA
    if token_recibido != TOKEN_SECRETO:
        return jsonify({"mensaje": "ACCESO DENEGADO: Token inválido"}), 401

    if coctel_solicitado in RECETAS:
        ingredientes = RECETAS[coctel_solicitado]
        print(f"\n[SERVIDOR] Iniciando preparación de: {coctel_solicitado.upper()}")
        
        # Simulación física de activación de motores en la terminal de tu laptop
        for liquido, tiempo in ingredientes.items():
            pin = MOTORES_VIRTUALES[liquido]["pin"]
            print(f" -> [PIN {pin}] MOTORES: Encendiendo bomba de {liquido}...")
            time.sleep(tiempo) # Simula el tiempo que dura bombeando el líquido
            print(f" -> [PIN {pin}] MOTORES: Apagando bomba de {liquido}. Dosis completada.")
            
        print("[SERVIDOR] ¡Coctel terminado listo para retirar!\n")
        return jsonify({"mensaje": f"¡Sirviendo {coctel_solicitado}! Revisa la terminal de tu laptop."})
    
    return jsonify({"mensaje": "Coctel no encontrado"}), 404

if __name__ == '__main__':
    # host='0.0.0.0' le dice a Flask que escuche a dispositivos externos (como tu celular)
    # puerto 5000 es el estándar de pruebas
    app.run(host='0.0.0.0', port=5000, debug=True)