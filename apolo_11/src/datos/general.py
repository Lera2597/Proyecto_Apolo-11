""" @Luis falta aquí un mejor docstring
"""
import random
import os
from yaml import load, SafeLoader, YAMLError

path_missions_conf: str = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'missions.yaml')
path_sys_conf: str = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'sys.yaml')


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
    limites.append(random.randint(1, cantidad))
    for i in range(num_particiones - 2):
        limites.append(random.randint(limites[i], cantidad))
    # Calcular las "num_particiones" partes
    partes: list = []
    partes.append(limites[0])
    for i in range(len(limites) - 1):
        partes.append(limites[i + 1] - limites[i])
    partes.append(cantidad - limites[-1])

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
            content = load(file, Loader=SafeLoader)
    except YAMLError as ex:  # @Luis mejoré el Exception para que no fuera tan amplio, no sé si ese sea
        print(ex)
        content = None
    return content
