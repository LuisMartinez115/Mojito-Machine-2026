# motores.py
import time
import threading
from config import MOTORES  # Importamos la configuración de los pines

def _apagar_bomba_despues_de_tiempo(liquido, tiempo):
    pin = MOTORES[liquido]["pin"]
    
    # AQUÍ IRÁ EL HARDWARE REAL:
    # motor = OutputDevice(pin, active_high=False)
    # motor.on()
    print(f" -> [PIN {pin}] Encendiendo bomba de {liquido}...")
    
    time.sleep(tiempo)
    
    # motor.off()
    print(f" -> [PIN {pin}] Apagando bomba de {liquido}. Dosis completada.")

def dispensar_coctel(receta_ingredientes):
    """Lanza hilos en paralelo para activar los motores al mismo tiempo"""
    print("\n==================================================")
    print("[ALERTA DE HARDWARE]: RECIBIENDO ORDEN DESDE EL CELULAR...")
    print("[MÁQUINA ACTIVADA]: Iniciando el vaciado de líquidos AHORA.")
    print("==================================================")
    for liquido, tiempo in receta_ingredientes.items():
        if liquido in MOTORES:
            hilo = threading.Thread(
                target=_apagar_bomba_despues_de_tiempo, 
                args=(liquido, tiempo)
            )
            hilo.start()