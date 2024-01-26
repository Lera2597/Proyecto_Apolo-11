import time
from apolo_11.src.archivos.gestor import crear_archivo_log
from apolo_11.src.datos.mission import Mission
from apolo_11.src.datos.general import (
    leer_yaml,
    Distribute_Register,
    path_missions_conf_file,
    path_sys_conf_file
)
def data_generator_init()-> None:
    """
    Simula o genera los registros de todos los dispositivos y misiones con un periodo de ejecución
    y durante un tiempo de simulacion establecidos en el archivo de configuración.
    
    """    
    data_missions:dict = leer_yaml(path_missions_conf_file)
    data_sys:dict = leer_yaml(path_sys_conf_file)
    print(data_missions)
    print(data_sys)
    simulation_time = data_sys.get("tiempo_simulacion",20)
    simulation_period = data_sys.get("periodo_simulacion",20)
    registers:list = []
    start_time_simulation = time.time()
    finish_simulation:bool = False
    finish_period:bool = False
    cont:int =0
    Simulation_Cycle_cont:int = 0
    while not finish_simulation:
        Simulation_Cycle_cont +=1
        finish_period = False
        if (time.time() - start_time_simulation)>simulation_time:
            finish_simulation = True
        else:
            start_time_period  = time.time()
            cont +=1
            cont_aster = 0
            print(f"Cycle #{Simulation_Cycle_cont}")
            registers.extend(Simulation_Cycle(data_missions,data_sys))
            time_elapsed_simulation = time.time() - start_time_simulation
            if(time_elapsed_simulation >= simulation_time):
                    time_elapsed_simulation = simulation_time
            aux2 =int(100*time_elapsed_simulation/simulation_time)
            print(f"Simulacion: [{'*'*aux2}{'.'*(100-aux2)}]{aux2}% ",end='\r')
            print("")
            #print(registers)
            contador = 1
            for register in registers:
                crear_archivo_log(register, contador)
                contador += 1
            registers.clear()
            
def Simulation_Cycle(data_missions_:dict,data_sys_:dict)->list:
    """
    Genera los registros de todos los dispositivos y misiones durante
    un periodo de simulacion
    
    :param data_missions_: Contiene informacion de las misones como 
    los nombres y dispositivos 
    :type data_missions_: dict
    :param data_sys_: Contiene la informacion la somimualcion como
    periodo y tiempo de simulacion
    :type data_sys_: dict
    :return: Lista con todos los regsitros
    :rtype: list
    """
    finish_period = False
    start_time_period  = time.time()
    simulation_period = data_sys_.get("periodo_simulacion",20)
    num_registers:int = data_sys_.get("num_registros",0)
    name_missions:list = data_missions_.get("mision","Error yaml: mision")
    name_devices:list = data_missions_.get("dispositivo","Error yaml: dispositivo")
    name_states:list = (data_missions_.get("estado_dispositivo",
                                        "Error yaml: Estado Dispositivo"))
    registers = []
    while not finish_period:
        time_elapsed_period = time.time() - start_time_period
        if(time_elapsed_period >= simulation_period):
            time_elapsed_period = simulation_period
        aux1 =int(100*time_elapsed_period/simulation_period)
        print(f"Perido:     [{'*'*aux1}{'.'*(100-aux1)}]{aux1}% ",end='\r')
        if time_elapsed_period >= simulation_period:   
            reg_per_mission:list = Distribute_Register(num_registers,len(name_missions))
            missions:list = []
            for i in range(len(name_missions)):
                if reg_per_mission[i] != 0:
                    missions.append(Mission(name_missions[i],reg_per_mission[i]))
            for mission in missions:
                reg = mission.Get_Registers(name_devices,name_states)
                registers.extend(reg)
            finish_period = True
            print("")
    return registers