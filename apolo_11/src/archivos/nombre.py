"""
Funcionalidad para generar el nombre de los archivos .log el formato estándar.
"""

from apolo_11.src.datos.general import leer_yaml, path_missions_conf, path_sys_conf


def generar_nombre_archivo(mission: str, numero: int) -> str:
    """
    Genera el nombre de un archivo .log basado en la misión y un número de archivo.

    :param mission: El nombre de una misión
    :type mission: str
    :param numero: El número del archivo.
    :type numero: int
    :raises ValueError: Error, si la misión no está dentro de las misiones permitidas.
    :raises ValueError: Error, si el número está fuera del rango para el nombre de los archivos.
    :raises ValueError: Error al generar el nombre del archivo
    :return: El nombre del archivo.
    :rtype: str
    """
    try:
        # Verificar si la misión es válida
        data_missions: dict = leer_yaml(path_missions_conf)
        data_sys: dict = leer_yaml(path_sys_conf)
        misiones_permitidas: list = data_missions.get("mision", "Error yaml: mision")
        min_value: int = data_sys.get("min_log_file", 1)
        max_value: int = data_sys.get("max_log_file", 1000)

        if mission not in misiones_permitidas:
            raise ValueError(f"Misión no válida. Debe ser una de las siguientes: {', '.join(misiones_permitidas)}")

        # Verificar si el número está en el rango especificado
        if not min_value <= numero <= max_value:
            raise ValueError(f"Número fuera del rango permitido ({min_value}-{max_value})")

        # Formatear el nombre del archivo
        return f"APL{mission}-{numero:05d}.log"

    except ValueError as ve:
        # Capturar y relanzar el error con un mensaje específico
        raise ValueError(f"Error al generar el nombre del archivo: {str(ve)}") from ve
