""" @Luis falta aquí un mejor docstring
"""

from datetime import datetime
from random import randint


class Device:
    """
    Establece el comportamiento de un dispositivo que genera registros
    con determinada información.
    """
    def __init__(self, name_mision: str, name_device: str, num_register: int) -> None:
        self.mision: str = name_mision
        self.name: str = name_device
        self.num_register: int = num_register
        self.date: str = datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(
            "-", ""
        ).replace(
            ":", ""
        ).replace(
            " ", ""
        )
        self.state: str = ""

    def get_registers(self, name_states_: list) -> list:
        """
        Genera una lista con la cantidad de registros provenientes
        de un unico dispositivo y de una adeterminada mision. Recibe una lista
        con todos los estados posibles que tendria el dispositivo para
        cada registro generado.

        :param name_states_:  Lista con todos los posibles estados que puede
        tener el dispositivo.
        :type name_states_: list
        :return: list: Lista con todos los regsitros generados por el dispositivo
        perteneciente a una determinada mision
        :rtype: list
        """
        name_states: list = name_states_
        return [{"date": self.date,
                 "mission": self.mision,
                 "device": self.name,
                 "state": name_states[randint(0, len(name_states) - 1)]} for _ in range(self.num_register)]
