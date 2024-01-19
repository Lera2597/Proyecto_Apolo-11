from .device import Device
from .general import (
    leer_yaml,
    Distribute_Register
)
class Mission:
    def __init__(self,name_mision:str,num_registers:int) -> None:
        self.name = name_mision
        self.num_register = num_registers
        self.registers:list = []
    def Get_Registers(self,name_devices_:list,name_states_:list)->list: 
        name_devices:list = name_devices_
        reg_per_dev:list = Distribute_Register(self.num_register,len(name_devices))
        devices = []
        for i in range(len(name_devices)):
            if(reg_per_dev[i] !=0):
                devices.append(Device(self.name,name_devices[i],reg_per_dev[i]))
        for disp in devices:
            reg = disp.Get_Registers(name_states_)
            self.registers.extend(reg)
        
        return self.registers