""" @Juliana falta aquí un mejor docstring
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
            contenido = (
                f"Fecha: {fecha_actual}\n"
                f"Misión: unknown\n"
                f"Tipo de Dispositivo: desconocido\n"
                f"Estado del Dispositivo: desconocido\n"
                f"Hash: unknown"
            )
        else:
            # Generar contenido con información completa y calcular hash
            contenido = (
                f"Fecha: {fecha_actual}\n"
                f"Misión: {device['mission']}\n"
                f"Tipo de Dispositivo: {device['device']}\n"
                f"Estado del Dispositivo: {device['state']}\n"
                f"Hash: {calcular_hash(fecha_actual, device)}"
            )

        return contenido

    except KeyError as e:  # @Juliana mejoré el Exception para que no fuera tan amplio
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
