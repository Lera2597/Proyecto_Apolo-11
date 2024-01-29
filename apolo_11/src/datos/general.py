""" Este módulo contiene funciones generales que pueden
    llamar y utulizar desde los otros módulos
"""

from random import randint
from os import path
from yaml import load, SafeLoader, YAMLError

path_missions_conf: str = path.join(path.dirname(__file__), '..', '..', 'config', 'missions.yaml')
path_sys_conf: str = path.join(path.dirname(__file__), '..', '..', 'config', 'sys.yaml')


def distribute_register(cantidad: int, num_particiones: int) -> list:
    """
    Reparte o distribuye el numero de regsitros en un numero
    de terminado de partes de manera aleatoria.

    _extended_summary_

    :param cantidad: Numero de registros
    :type cantidad: int
    :param num_particiones: Numero de partisiones
    :type num_particiones: int
    :return: Lista con la cantidad de registros por particion
    :rtype: list
    """
    # Generar "num_particiones"-1 números aleatorios que representan los límites
    limites: list = []
    limites.append(randint(1, cantidad))
    for i in range(num_particiones - 2):
        limites.append(randint(limites[i], cantidad))
    # Calcular las "num_particiones" partes
    partes: list = []
    partes.append(limites[0])
    for i in range(len(limites) - 1):
        partes.append(limites[i + 1] - limites[i])
    partes.append(cantidad - limites[-1])

    return partes

def numero_registers(l_inferior: int, l_superior: int) -> int:
    """
    permiete generar un numero entero aleatorio dentro de 
    los limites ingresados
    :param l_inferior: valor del limite inferior
    :type l_inferior: int
    :param l_superior: valor del limite superior
    :type l_superior: int
    :return: Valor aleatorio 
    :rtype: int
    """
    return randint(l_inferior, l_superior)

def leer_yaml(route: str) -> dict:
    """permite leer un archivo yaml y devolver el contenido como dict

    :param route: ruta archivo
    :type path: str
    :return: rdiccionario con los datos YAML, de lo contrario devuelve Ninguno
    :rtype: dict
    """
    content: dict = None
    try:
        with open(route, encoding="utf-8") as file:
            content = load(file, Loader=SafeLoader)
    except YAMLError as ex:  # @Luis mejoré el Exception para que no fuera tan amplio, no sé si ese sea
        print(ex)
        content = None
    return content


def numero_registers(l_inferior: int, l_superior: int) -> int:
    """
    permiete generar un numero entero aleatorio dentro de
    los limites ingresados
    :param l_inferior: valor del limite inferior
    :type l_inferior: int
    :param l_superior: valor del limite superior
    :type l_superior: int
    :return: Valor aleatorio
    :rtype: int
    """
    return randint(l_inferior, l_superior)
