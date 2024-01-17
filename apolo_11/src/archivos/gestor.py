from pathlib import Path
from shutil import move
from datetime import datetime
from src.archivos.nombre import generar_nombre_archivo
from src.archivos.contenido import generar_contenido_log 



def crear_archivo_log(device: dict, numero: int) -> bool:
    """
    Crea un archivo .log y lo guarda en el directorio "devices".

    :param directorio_salida: Ruta del directorio donde se guardará el archivo .log.
    :type directorio_salida: str
    :param nombre_mision: El nombre de la misión.
    :type nombre_mision: str
    :param tipo_dispositivo: El tipo de dispositivo.
    :type tipo_dispositivo: str
    :param estado_dispositivo: El estado del dispositivo.
    :type estado_dispositivo: str
    :param numero: El número del archivo.
    :type numero: int
    :param num_registers: Número de registros a generar en la misión.
    :type num_registers: int
    :return: True si se creó con éxito el archivo, False en caso contrario.
    :rtype: bool
    """
    try:
        # Crear el directorio si no existe
        directorio_salida = Path('devices')
        directorio_salida.mkdir(exist_ok=True)

        #for i in range(num_registers):
        # Obtener el nombre del archivo utilizando la función generar_nombre_archivo
        #mision = Mission(name_mision=nombre_mision, num_registers=num_registers)
        nombre_archivo = generar_nombre_archivo(device['mission'], numero)  

        # Construir la ruta completa del archivo
        ruta_completa = directorio_salida / nombre_archivo

            # Obtener el contenido utilizando la función generar_contenido_log
        #device = Device(name_mision=nombre_mision, name_device=tipo_dispositivo, num_registers=num_registers)
        contenido = generar_contenido_log(device)

            # Abrir el archivo y escribir el contenido
        with ruta_completa.open('w') as file:
                file.write(contenido)

        return True  # Indica que se crearon los archivos con éxito

    except FileNotFoundError as e:
        print(f"Error: No se pudo encontrar o crear el directorio {directorio_salida}. {e}")
        return False

    except IOError as e:
        print(f"No se pudo guardar el archivo {ruta_completa}: {e}")
        return False

    except Exception as e:
        # Captura de excepciones generales
        print(f"Error al crear el archivo: {e}")
        return False




def realizar_copia_seguridad(directorio_salida: str) -> bool:
    """
    Realiza una copia de seguridad de los archivos .log en un directorio llamado 'backup'.
    Crea una subcarpeta con el nombre de la fecha actual en formato ddmmyyHHMISS.
    Mueve los archivos .log a la subcarpeta correspondiente.

    :param directorio_salida: Ruta del directorio donde se encuentran los archivos .log.
    :type directorio_salida: str
    :return: True si se realizó la copia de seguridad con éxito, False en caso contrario.
    :rtype: bool
    """
    try:
        # Crear el directorio de backups si no existe
        directorio_backups = Path("backup")
        directorio_backups.mkdir(exist_ok=True)

        # Crear una subcarpeta con el nombre de la fecha actual
        fecha_actual = datetime.now().strftime('%d%m%y%H%M%S')
        subdirectorio_backup = directorio_backups / fecha_actual
        subdirectorio_backup.mkdir(exist_ok=True)

        # Mover los archivos .log al directorio de backups
        for archivo_log in Path(directorio_salida).glob("*.log"):
            move(archivo_log, subdirectorio_backup / archivo_log.name)

        return True  # Indica que se realizó con éxito la copia de seguridad

    except Exception as e:
        print(f"No se pudo realizar la copia de seguridad: {e}")
        return False
