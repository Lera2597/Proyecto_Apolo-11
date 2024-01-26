from pathlib import Path

def test_device(app):
    response = app.Fun_Get_registers_device(["Bueno","Regular","Malo"])
    
    assert type(response) == list
    assert len(response) == 3
    assert type(response[0]) == dict
    assert len(response[0].keys()) == 4
    
def test_mission(app):
    response = app.Fun_Get_registers_mission(["device_1","device_2","device_3"],["Bueno","Regular","Malo"])
    assert type(response) == list
    assert len(response) == 10
    assert type(response[0]) == dict
    assert len(response[0].keys()) == 4
    
def test_general_Leer_Yaml(app):
    path_file:str = Path("apolo_11","config","missions.yaml")
    response = app.Fun_Leer_Yaml(path_file)
    assert type(response) == dict
    
def test_generator_simulation_Clicle(app):

    data_missions:dict = {
        "mision": ["ORBONE","CLNM", "TMRS","GALXONE","UNKN"],
        "dispositivo": [ "satelite","nave espacial","vehiculo espacial","traje espacial","robot espacial"],
        "estado_dispositivo": ["excelente", "bueno", "advertencia","defectuoso","inoperable","desconocido"]
        }
    data_sys:dict= {"periodo_simulacion": 10, "tiempo_simulacion": 60, "num_registros": 50}
    response = app.Fun_Simulation_Cicle(data_missions,data_sys)
    assert type(response) == list
    assert len(response) == data_sys["num_registros"]