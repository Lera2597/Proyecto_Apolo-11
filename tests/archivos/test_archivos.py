"""_summary_
"""
# from pathlib import Path


def test_nombre(app):
    """_summary_

    :param app: _description_
    :type app: _type_
    """
    mission: str = "ORBONE"
    id_: int = 1
    response = f"APL{mission}-{id_:05d}.log"
    assert app.fun_generar_nombre_archivo(mission, id_) == response


def test_gestor(app):
    """_summary_

    :param app: _description_
    :type app: _type_
    """
    # file_path = Path("Proyecto_Apolo-11", "tests", "Archivos_test")
    registro: dict = {'date': '26012024215450', 'mission': 'ORBONE', 'device': 'satelite', 'state': 'excelente'}
    id_: int = 1
    assert app.fun_crear_archivo_log("Result_test", registro, id_) is True
