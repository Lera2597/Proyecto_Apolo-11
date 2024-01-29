"""_summary_
"""
from pathlib import Path


def test_device(app) -> None:
    """_summary_

    :param app: _description_
    :type app: _type_
    """
    response = app.fun_get_registers_device(["Bueno", "Regular", "Malo"])

    assert isinstance(response, list)
    assert len(response) == 3
    assert isinstance(response[0], dict)
    assert len(response[0].keys()) == 4


def test_mission(app) -> None:
    """_summary_

    :param app: _description_
    :type app: _type_
    """
    response = app.fun_get_registers_mission(["device_1", "device_2", "device_3"], ["Bueno", "Regular", "Malo"])
    assert isinstance(response, list)
    assert len(response) == 10
    assert isinstance(response[0], dict)
    assert len(response[0].keys()) == 4


def test_general_leer_yaml(app) -> None:
    """_summary_

    :param app: _description_
    :type app: _type_
    """
    path_file: str = Path("apolo_11", "config", "missions.yaml")
    response = app.fun_leer_yaml(path_file)
    assert isinstance(response, dict)


def test_generator_simulation_cicle(app) -> None:
    """_summary_

    :param app: _description_
    :type app: _type_
    """
    data_missions: dict = {
        "mision": ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"],
        "dispositivo": ["satelite", "nave espacial", "vehiculo espacial", "traje espacial", "robot espacial"],
        "estado_dispositivo": ["excelente", "bueno", "advertencia", "defectuoso", "inoperable", "desconocido"]}
    data_sys: dict = {"periodo_simulacion": 2, "tiempo_simulacion": 10}
    num_registers: int = 10
    response = app.fun_simulation_cicle(data_missions, data_sys, num_registers)
    assert isinstance(response, list)
    assert len(response) == num_registers
