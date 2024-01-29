"""Contiene las funciones de prueba para el
    paquete de archivos.
"""


def test_nombre(app):
    """test para el módulo nombre

    :param app: Variable de llamado para la invocación de la función
    :type app: App
    """
    mission: str = "ORBONE"
    id_: int = 1
    response = f"APL{mission}-{id_:05d}.log"
    assert app.fun_generar_nombre_archivo(mission, id_) == response


def test_gestor(app) -> None:
    """ Funcionalidad para probar el archivo gestor

    :param app: Variable de llamado para la invocación de la función
    :type app: App
    """
    registro: dict = {'date': '26012024215450', 'mission': 'ORBONE', 'device': 'satelite', 'state': 'excelente'}
    id_: int = 1
    assert app.fun_crear_archivo_log("Result_test", registro, id_) is True
