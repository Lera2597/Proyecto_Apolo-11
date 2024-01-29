""" @Luis falta aquí un mejor docstring
"""

from .device import Device
from .general import (
    distribute_register
)


class Mission:
    """
    Establece el comportamiento de una mision que tiene asociados dispositivos
    que generan registros con determinada información.
    """
    def __init__(self, name_mision: str, num_registers: int) -> None:
        self.name: str = name_mision
        self.num_register: int = num_registers
        self.registers: list = []

    def get_registers(self, name_devices_: list, name_states_: list) -> list:
        """
        Genera una lista con la cantidad de registros provenientes
        de todos los dispositivos y de la mision. Recibe una lista
        con todos los estados posibles que tendran los dispositivos para
        cada registro generado. Ademas recibe el nombre que se le asigara
        a cada dispositivo.

        :param name_devices_: Lista con todos los posiblesnombres que puede
        tener el dispositivo.
        :type name_devices_: list
        :param name_states_: Lista con todos los posibles estados que puede
        tener el dispositivo.
        :type name_states_: list
        :return: Lista con todos los registros generados por todos los dispositivos
        pertenecientes a la mision.
        :rtype: list
        """
        name_devices: list = name_devices_
        reg_per_dev: list = distribute_register(self.num_register, len(name_devices))
        devices: list = []
        fin: int = len(name_devices)
        for i in range(fin):
            if reg_per_dev[i] != 0:
                devices.append(Device(self.name, name_devices[i], reg_per_dev[i]))
        for disp in devices:
            reg = disp.get_registers(name_states_)
            self.registers.extend(reg)

        return self.registers
