#from src.datos.mission import Mission
from src.datos.device import Device
import hashlib
from datetime import datetime

def generar_contenido_log(device: dict) -> str:
    """
    Genera el contenido para un archivo .log con información semiestructurada.

    :param device: Objeto de tipo Device.
    :type device: Device
    :return: Contenido del archivo .log generado.
    :rtype: str
    """
    try:
        # Generar la fecha actual en el formato ddmmyyHHMISS
        fecha_actual = device['date']#datetime.now().strftime('%d%m%y%H%M%S')
        
        # Verificar si la misión es conocida o desconocida
        if device['mission'] == "UNKN":
            # En caso de misión desconocida, utilizar solo fecha el resto es UNKN
            contenido = f"Fecha: {fecha_actual}\nMisión: unknown\nTipo de Dispositivo: {device['device']}\nEstado del Dispositivo: {device['state']}\nHash: unknown"
        else:
            # Generar contenido con información completa y calcular hash
            contenido = f"Fecha: {fecha_actual}\nMisión: {device['mission']}\nTipo de Dispositivo: {device['device']}\nEstado del Dispositivo: {device['state']}\nHash: {calcular_hash(fecha_actual, device)}"
            
        return contenido

    except Exception as e:
        # Manejo de errores
        mensaje_error = f"Error al generar el contenido del archivo .log: {str(e)}"
        return mensaje_error



def calcular_hash(fecha: str, device: dict) -> str:
    """
    Calcula el hash basado en la fecha, misión, tipo de dispositivo y estado del dispositivo.

    :param fecha: La fecha en el formato ddmmyyHHMISS.
    :type fecha: str
    :param device: Objeto de tipo Device.
    :type device: Device
    :return: El hash calculado.
    :rtype: str
    """
    if device['mission'] == "UNKN":
        return "unknown"  # No se genera el hash para archivos con misión desconocida

    # Concatenar los datos
    datos_concatenados = f"{fecha}{device['mission']}{device['device']}{device['state']}"

    # Calcular el hash utilizando SHA-256
    hash_obj = hashlib.sha256(datos_concatenados.encode())
    hash_calculado = hash_obj.hexdigest()

    return hash_calculado
