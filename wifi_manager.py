# wifi_manager.py
import subprocess
import time
from flask import Flask, render_template_string, request

app = Flask(__name__)

def obtener_ssids_disponibles():
    try:
        resultado = subprocess.check_output(["nmcli", "-t", "-f", "SSID,SIGNAL", "device", "wifi", "list"], text=True)
        redes = []
        for linea in resultado.strip().split("\n"):
            if ":" in linea:
                ssid, senal = linea.split(":")
                if ssid and ssid not in [r['ssid'] for r in redes]:
                    redes.append({"ssid": ssid, "senal": senal})
        return redes
    except Exception: return []

def esta_conectado():
    try:
        salida = subprocess.check_output(["nmcli", "-t", "-f", "DEVICE,STATE", "device"], text=True)
        return "wlan0:connected" in salida.replace(" ", "")
    except Exception: return False

HTML_PORTAL = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Configurar Coctelera</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1e1e24; color: #fff; text-align: center; padding: 20px; }
        h2 { color: #00adb5; }
        select, input { width: 90%; max-width: 300px; padding: 12px; margin: 10px 0; border-radius: 8px; border: none; font-size: 16px; }
        input[type="submit"] { background: #00adb5; color: white; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <h2>⚙️ CONFIGURACIÓN WI-FI</h2>
    <form action="/conectar" method="POST">
        <select name="ssid" required>
            <option value="">-- Seleccionar Red --</option>
            {% for red in lista_redes %}
                <option value="{{ red.ssid }}">{{ red.ssid }} (⚡ {{ red.senal }}%)</option>
            {% endfor %}
        </select><br>
        <input type="password" name="password" placeholder="Contraseña" required><br>
        <input type="submit" value="Conectar Coctelera">
    </form>
</body>
</html>
"""

@app.route('/')
def portal():
    return render_template_string(HTML_PORTAL, lista_redes=obtener_ssids_disponibles())

@app.route('/conectar', methods=['POST'])
def conectar():
    ssid = request.form.get('ssid')
    password = request.form.get('password')
    # Ejecuta en segundo plano la conexión para no trabar la web
    subprocess.Popen(["sudo", "nmcli", "device", "wifi", "connect", ssid, "password", password])
    return "<h3>Conectando... En unos segundos la coctelera estará lista en la red local.</h3>"

if __name__ == '__main__':
    print("[SISTEMA] Verificando conexión...")
    time.sleep(4)
    if esta_conectado():
        print("[SISTEMA] Wi-Fi detectado. Arrancando coctelera normal...")
        # 🚀 LANZA EL SEGUNDO SCRIPT AUTOMÁTICAMENTE
        subprocess.run(["python", "app.py"])
    else:
        print("[SISTEMA] Sin red. Levantando Portal Cautivo...")
        try:
            subprocess.run(["sudo", "nmcli", "device", "wifi", "hotspot", "ssid", "Configurar_Coctelera"], check=True)
            app.run(host='0.0.0.0', port=5000, debug=False)
        except Exception as e:
            print(f"Error: {e}")