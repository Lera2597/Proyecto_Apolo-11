import time
from src.archivos.gestor import crear_archivo_log
from .mission import Mission
from .general import (
    leer_yaml,
    Distribute_Register,
    path_missions_conf,
    path_sys_conf
)
def data_generator_init()-> list:
    """Esta funcion es encarga de generar los registros de todos 
    los dispositivos y misiones. 

    Returns:
        list: Lista con todos los registros generados
    """
    data_missions:dict = leer_yaml(path_missions_conf)
    data_sys:dict = leer_yaml(path_sys_conf)
    simulation_time = data_sys.get("tiempo_simulacion",20)
    simulation_period = data_sys.get("periodo_simulacion",20)
    registers:list = []
    start_time_simulation = time.time()
    finish_simulation:bool = False
    finish_period:bool = False
    cont:int =0
    while not finish_simulation:
        
        finish_period = False
        if (time.time() - start_time_simulation)>simulation_time:
            finish_simulation = True
        else:
            start_time_period  = time.time()
            cont +=1
            while not finish_period:
                if (time.time() - start_time_period)> simulation_period:                  
                    num_registers:int = data_sys.get("num_registros",0)
                    name_missions:list = data_missions.get("mision","Error yaml: mision")
                    name_devices:list = data_missions.get("dispositivo","Error yaml: dispositivo")
                    name_states:list = data_missions.get("estado_dispositivo","Error yaml: Estado Dispositivo")
                    reg_per_mission:list = Distribute_Register(num_registers,len(name_missions))
                    missions:list = []
                    for i in range(len(name_missions)):
                        if(reg_per_mission[i] != 0):
                            missions.append(Mission(name_missions[i],reg_per_mission[i]))
                    for mission in missions:
                        reg = mission.Get_Registers(name_devices,name_states)
                        registers.extend(reg) 
                    finish_period = True
            print(registers)
            contador = 1
            for register in registers:
                crear_archivo_log(register, contador)
                contador += 1
            
            
            print()
            print()
            registers.clear()
    return [cont] 