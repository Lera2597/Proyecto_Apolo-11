"""para definir configuración transversal que pueden ser usados 
en las diferentes pruebas unitarias.

todas las pruebas unitarias normalmente se hacen con funciones y asserts
"""
import pytest
from apolo_11.src.datos.device import Device
from apolo_11.src.datos.mission import Mission
from apolo_11.src.datos.general import leer_yaml
from apolo_11.src.datos.data_generator import Simulation_Cycle
from apolo_11.src.archivos.nombre import generar_nombre_archivo
from apolo_11.src.archivos.gestor import  crear_archivo_log
@pytest.fixture(scope="session")
def app():
    class App:
        pass
    app_ = App()
    device = Device("my_mission","robot",3)
    mission = Mission("my_mission",10)
    
    app_.Fun_Get_registers_device = device.Get_Registers
    app_.Fun_Get_registers_mission = mission.Get_Registers
    app_.Fun_Leer_Yaml = leer_yaml
    app_.Fun_Simulation_Cicle = Simulation_Cycle
    app_.Fun_Generar_Nombre_Archivo = generar_nombre_archivo
    app_.Fun_Crear_Archivo_Log = crear_archivo_log
    #agregar funciones a probar
    return app_