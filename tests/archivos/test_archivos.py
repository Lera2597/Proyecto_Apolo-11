"""Contiene las funciones de prueba para el
    paquete de archivos.
"""
# from pathlib import Path


def test_nombre(app):
    """test para el módulo nombre

    :param app: Clase que contien las funciones
    de los diferentes modulos a probar.
    :type app: _type_
    """
    mission: str = "ORBONE"
    id_: int = 1
    response = f"APL{mission}-{id_:05d}.log"
    assert app.fun_generar_nombre_archivo(mission, id_) == response


def test_gestor(app):
    """test para el módulo gestor

    :param app: Clase que contien las funciones
    de los diferentes modulos a probar.
    :type app: _type_
    """
    # file_path = Path("Proyecto_Apolo-11", "tests", "Archivos_test")
    registro: dict = {'date': '26012024215450', 'mission': 'ORBONE', 'device': 'satelite', 'state': 'excelente'}
    id_: int = 1
    assert app.fun_crear_archivo_log("Result_test", registro, id_) is True
