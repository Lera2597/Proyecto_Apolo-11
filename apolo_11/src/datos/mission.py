"""_summary_

:return: _description_
:rtype: _type_
"""
from .device import Device
from .general import (
    Distribute_Register
)
class Mission:
    """_summary_
    """
    def __init__(self,name_mision:str,num_registers:int) -> None:
        self.name = name_mision
        self.num_register = num_registers
        self.registers:list = []
    def Get_Registers(self,name_devices_:list,name_states_:list)->list:
        """Genera una lista con la cantidad de registros provenientes
        de todos los dispositivos y de la mision. Recibe una lista 
        con todos los estados posibles que tendran los dispositivos para 
        cada registro generado. Ademas recibe el nombre que se le asigara 
        a cada dispositivo.

        Args:
            name_devices_ (list): Lista con todos los posiblesnombres que puede 
            tener el dispositivo.
            name_states_ (list): Lista con todos los posibles estados que puede 
            tener el dispositivo.

        Returns:
            list: Lista con todos los registros generados por todos los dispositivos 
            pertenecientes a la mision.
        """
        name_devices:list = name_devices_
        reg_per_dev:list = Distribute_Register(self.num_register,len(name_devices))
        devices = []
        for i in range(len(name_devices)):
            if reg_per_dev[i] !=0:
                devices.append(Device(self.name,name_devices[i],reg_per_dev[i]))
        for disp in devices:
            reg = disp.Get_Registers(name_states_)
            self.registers.extend(reg)

        return self.registers
