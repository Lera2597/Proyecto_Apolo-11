import random
import datetime

class Device:
    """
    Establece el comportamiento de un dispositivo que genera registros
    con determinada información.
    """    
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
        name_states:list = name_states_
        return [{"date":self.date,
                    "mission":self.mision,
                    "device":self.name,
                    "state": name_states[random.randint(0,len(name_states)-1)]} for _ in range(self.num_register)]
