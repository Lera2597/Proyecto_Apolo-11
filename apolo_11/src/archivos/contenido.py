"""_summary_

Returns:
    _type_: _description_
"""
import hashlib


def generar_contenido_log(device: dict) -> str:
    """
    Genera el contenido para los archivos .log basado en los datos recibidos.

    :param device: Diccionario con los datos de los archivos .log
    :type device: dict
    :return: El contenido de los archivos .log
    :rtype: str
    """
    try:
        # Generar la fecha actual
        fecha_actual = device['date']

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

    :param fecha: La fecha actual en el formato ddmmyyHHMISS.
    :type fecha: str
    :param device: Diccionario que contiene los datos de las misiones
    :type device: dict
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
