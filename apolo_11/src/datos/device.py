import random
import datetime
from .general import (
    leer_yaml
)
class Device:
    def __init__(self,name_mision:str,name_device:str,num_register:int) -> None:
        self.mision = name_mision
        self.name = name_device
        self.num_register = num_register
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(
            "-",""
        ).replace(
            ":",""
        ).replace(
            " ",""
        )
        self.state:str = ""
        
    def Get_Registers(self,name_states_:list)->list:
        name_states:list = name_states_
        return [{"date":self.date,
                    "mission":self.mision,
                    "device":self.name,
                    "state": name_states[random.randint(0,len(name_states)-1)]} for _ in range(self.num_register)] 