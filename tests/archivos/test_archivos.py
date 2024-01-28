def test_nombre(app):
    mission:str = "ORBONE"
    id:int = 1
    response = f"APL[{mission}]-{id:05d}.log"
    assert app.Fun_Generar_Nombre_Archivo(mission,id) == response
    
def test_gestor(app):
    registro:dict = {'date': '26012024215450', 'mission': 'ORBONE', 'device': 'satelite', 'state': 'excelente'}
    id:int = 1
    assert app.Fun_Crear_Archivo_Log(registro, id) == True