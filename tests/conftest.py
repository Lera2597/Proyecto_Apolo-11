"""para definir configuración transversal que pueden ser usados
en las diferentes pruebas unitarias.

todas las pruebas unitarias normalmente se hacen con funciones y asserts
"""
import pytest
from apolo_11.src.datos.device import Device
from apolo_11.src.datos.mission import Mission
from apolo_11.src.datos.general import leer_yaml
from apolo_11.src.datos.data_generator import simulation_cycle
from apolo_11.src.archivos.nombre import generar_nombre_archivo
from apolo_11.src.archivos.gestor import crear_archivo_log


@pytest.fixture(scope="session")
def app():
    """Centralización de las funciones a probar dentro de las pruebas unitarias

    :return: Variable con la configuración de las funciones configuradas
    :rtype: App
    """
    class App:
        """_summary_
        """
        pass
    app_ = App()
    device = Device("my_mission", "robot", 3)
    mission = Mission("my_mission", 10)

    app_.fun_get_registers_device = device.get_registers
    app_.fun_get_registers_mission = mission.get_registers
    app_.fun_leer_yaml = leer_yaml
    app_.fun_simulation_cicle = simulation_cycle
    app_.fun_generar_nombre_archivo = generar_nombre_archivo
    app_.fun_crear_archivo_log = crear_archivo_log
    # agregar funciones pendientes a probar
    return app_
