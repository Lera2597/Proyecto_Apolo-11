import random
import os
import yaml
from yaml.loader import SafeLoader

path_missions_conf:str = os.path.join(os.path.dirname(__file__),'..','..','config','missions.yaml')
path_sys_conf:str = os.path.join(os.path.dirname(__file__),'..','..','config','sys.yaml')
def Distribute_Register(cantidad:int,num_particiones:int)->list:
    """
    Reparte o distribuye el valor de "cantidad" en "num_particiones" partes de manera aleatoria
    Args:
        cantidad (int): _description_
        num_particiones (int): _description_

    Returns:
        list: _description_
    """
    # Generar "num_particiones"-1 números aleatorios que representan los límites
    limites = []
    limites.append(random.randint(1, cantidad))
    for i in range(num_particiones-2):
        limites.append(random.randint(limites[i], cantidad))
    # Calcular las "num_particiones" partes
    partes = []
    partes.append(limites[0])
    for i in range(len(limites)-1):
        partes.append(limites[i+1]-limites[i])
    partes.append(cantidad-limites[-1])

    return partes

def leer_yaml(path: str) -> dict:
    """permite leer un archivo yaml y devolver el contenido como dict

    :param path: ruta archivo
    :type path: str
    :return: rdiccionario con los datos YAML, de lo contrario devuelve Ninguno
    :rtype: dict
    """
    content: dict = None
    try:
        with open(path) as file:
            content = yaml.load(file, Loader=SafeLoader)
    except Exception as ex:
        print(ex)
        content = None
    return content