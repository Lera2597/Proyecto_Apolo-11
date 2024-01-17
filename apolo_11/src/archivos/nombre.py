from src.datos.mission import Mission

def generar_nombre_archivo(mission: str, numero: int) -> str:
    """
    Genera el nombre de un archivo .log basado en la misión y el número.

    :param mission: Objeto de tipo Mission.
    :type mission: Mission
    :param numero: El número del archivo.
    :type numero: int
    :return: El nombre del archivo.
    :rtype: str
    :raises ValueError: Si el número está fuera del rango o la misión no es válida.
    """
    try:
        # Verificar si la misión es válida
        misiones_permitidas = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
        if mission not in misiones_permitidas:
            raise ValueError(f"Misión no válida. Debe ser una de las siguientes: {', '.join(misiones_permitidas)}")

        # Verificar si el número está en el rango especificado
        if not (1 <= numero <= 1000):
            raise ValueError(f"Número fuera del rango permitido (1-{numero:05d})")

        # Formatear el nombre del archivo
        return f"APL[{mission}]-{numero:05d}.log"

    except ValueError as ve:
        # Capturar y relanzar el error con un mensaje específico
        raise ValueError(f"Error al generar el nombre del archivo: {str(ve)}")
