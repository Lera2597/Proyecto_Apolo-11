""" Este módulo contiene el proceso de generar o simular durante
un tiempo establecido los registros para los diferentes 
dispositivos y misiones.

"""

from time import time
from apolo_11.src.archivos.gestor import crear_archivo_log
from apolo_11.src.datos.mission import Mission
from apolo_11.src.datos.general import (
    leer_yaml,
    distribute_register,
    path_missions_conf,
    path_sys_conf,
    numero_registers
)


def data_generator_init(path_salida: str) -> None:
    """
    Simula o genera los registros de todos los dispositivos y misiones con un periodo de ejecución
    y durante un tiempo de simulacion establecidos en el archivo de configuración.
    """
    
    data_missions: dict = leer_yaml(path_missions_conf)
    data_sys: dict = leer_yaml(path_sys_conf)
    simulation_time: int = data_sys.get("tiempo_simulacion", 20)
    min_log_file: int = data_sys.get("min_log_file", 1)
    registers: list = []
    start_time_simulation: float = time()
    finish_simulation: bool = False
    cont: int = 0
    simulation_cycle_cont: int = 0
    name_missions: list = data_missions.get("mision", "Error yaml: mision")
    dict_cont: dict = {valor: {"contador": min_log_file} for valor in name_missions}
    while not finish_simulation:
        simulation_cycle_cont += 1
        if (time() - start_time_simulation) > simulation_time:
            finish_simulation = True
        else:
            cont += 1
            print(f"Ciclo # {simulation_cycle_cont}")
            num_registers: int = numero_registers(data_sys.get("min_num_reg", 1),data_sys.get("max_num_reg", 100) )
            registers.extend(simulation_cycle(data_missions, data_sys,num_registers))
            time_elapsed_simulation: float = time() - start_time_simulation
            time_elapsed_simulation = min(time_elapsed_simulation, simulation_time)
            aux2 = int(100 * time_elapsed_simulation / simulation_time)
            print(f"Simulación: [{'*'*aux2}{'.'*(100-aux2)}]{aux2}% ", end='\r')
            print("")
            for register in registers:
                crear_archivo_log(path_salida, register, dict_cont[register["mission"]]["contador"])
                dict_cont[register["mission"]]["contador"] += 1
            registers.clear()


def simulation_cycle(data_missions_: dict, data_sys_: dict, num_registers: int) -> list:
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
    start_time_period: float = time()
    simulation_period: int = data_sys_.get("periodo_simulacion", 20)
    print(num_registers)
    name_missions: list = data_missions_.get("mision", "Error yaml: mision")
    name_devices: list = data_missions_.get("dispositivo", "Error yaml: dispositivo")
    name_states: list = data_missions_.get("estado_dispositivo", "Error yaml: Estado Dispositivo")
    registers: list = []
    while not finish_period:
        time_elapsed_period: float = time() - start_time_period
        time_elapsed_period = min(time_elapsed_period, simulation_period)
        aux1 = int(100 * time_elapsed_period / simulation_period)
        print(f"Período:    [{'*'*aux1}{'.'*(100-aux1)}]{aux1}% ", end='\r')
        if time_elapsed_period >= simulation_period:
            reg_per_mission: list = distribute_register(num_registers, len(name_missions))
            missions: list = []
            fin: int = len(name_missions)
            for i in range(fin):
                if reg_per_mission[i] != 0:
                    missions.append(Mission(name_missions[i], reg_per_mission[i]))
            for mission in missions:
                reg = mission.get_registers(name_devices, name_states)
                registers.extend(reg)
            finish_period = True
            print("")
    return registers
