""" @Juliana falta aquí un mejor docstring
"""
from pathlib import Path
from typing import List, Dict
from pydantic import BaseModel
from prettytable import PrettyTable


class DeviceLog(BaseModel):
    """
    El objeto DeviceLog es una instancia de la clase BaseModel de Pydantic y se utiliza
    para modelar la estructura de los datos que se extraen de los archivos .log
    """
    fecha: str
    mision: str
    tipo_dispositivo: str
    estado_dispositivo: str
    hash: str


def parse_log_file(content: str) -> DeviceLog:
    """
    Parsea (procesa) el contenido de un archivo de registro (.log) y devuelve un objeto DeviceLog.

    :param content: Contenido del archivo de registro.
    :type content: str
    :return: Objeto DeviceLog con la información del archivo.
    :rtype: DeviceLog
    """
    # Dividir el contenido del archivo en líneas
    lines = content.split('\n')

    # Verificar si hay suficientes líneas para procesar
    if len(lines) < 5:
        raise ValueError("El formato del archivo de registro es incorrecto.")

    try:
        # Extracción de datos del archivo
        fecha = lines[0].split(":")[1].strip()
        mision = lines[1].split(":")[1].strip()
        tipo_dispositivo = lines[2].split(":")[1].strip()
        estado_dispositivo = lines[3].split(":")[1].strip()
        hash_value = lines[4].split(":")[1].strip()

        return DeviceLog(
            fecha=fecha,
            mision=mision,
            tipo_dispositivo=tipo_dispositivo,
            estado_dispositivo=estado_dispositivo,
            hash=hash_value
        )
    except IndexError as e:
        raise ValueError(f"Error al extraer datos del archivo de registro: {str(e)}") from e


def extract_logs_from_folder(folder_path: Path) -> List[DeviceLog]:
    """
    Extrae logs de archivos en la carpeta especificada.

    :param folder_path: Ruta a la carpeta que contiene los archivos de registro.
    :type folder_path: Path
    :return: Lista de objetos DeviceLog.
    :rtype: List[DeviceLog]
    """
    logs = []
    for file_path in folder_path.glob("*.log"):
        try:
            # print(f"Procesando archivo: {file_path}") @Juliana se comenta ya que no es necesario en la ejecución final
            with open(file_path, "r") as file:  # @Juliana, aquí pide usar encoding, pero no supe dar con cual
                content = file.read()
            log = parse_log_file(content)
            logs.append(log)
        except (IOError, UnicodeDecodeError) as e:  # @Juliana mejoré el Exception para que no fuera tan amplio
            print(f"Error al procesar el archivo {file_path}: {str(e)}")

    return logs


def table_decorator(header: str) -> callable:
    """
    Un decorador para agregar un encabezado y una línea de guiones encima de una tabla
    generada por una función. El propósito principal de esta función es proporcionar un
    encabezado para las tablas generadas.

    :param header: El encabezado que se agregará encima de la tabla.
    :type header: str
    :return: Un decorador que se puede aplicar a funciones que generan tablas.
    :rtype: callable

    Uso:
    ```python
    @table_decorator("Tabla de Ejemplo")
    def generate_example_table():
        table = PrettyTable()
        table.field_names = ["Columna1", "Columna2"]
        table.add_row(["Dato1", "Dato2"])
        return str(table)
    ```
    """
    def decorator(func):
        """
        Esta es la función interna del decorador que toma otra función (func) como argumento.
        """
        def wrapper(*args, **kwargs):
            """
            Esta es otra función interna que toma cualquier número de argumentos posicionales (*args)
            y argumentos de palabra clave (**kwargs). Esta función agrega el encabezado al resultado.
            """
            table = func(*args, **kwargs)
            return f"{header}\n{'=' * len(header)}\n{table}\n"
        return wrapper
    return decorator


@table_decorator("Tabla 1: Cantidad total de eventos por estado para cada misión y dispositivo")
def gsct(state_count: Dict):  # generate_state_count_table
    """ @Juliana falta aquí un mejor docstring
    """
    # Diccionario para realizar el seguimiento de las sumas por Tipo de Dispositivo, Misión y Estado
    total_count_by_device_mission_state = {}

    # Iterar sobre los elementos del estado y contar
    for key, count in state_count.items():
        mission, device, state = key

        # Excluir la misión "UNKN"
        if mission == "UNKN":
            continue

        # Verificar si ya existe la entrada en el diccionario, si no, inicializarla
        if (device, mission, state) not in total_count_by_device_mission_state:
            total_count_by_device_mission_state[(device, mission, state)] = 0

        # Sumar al total de eventos por Tipo de Dispositivo, Misión y Estado
        total_count_by_device_mission_state[(device, mission, state)] += count

    # Crear la tabla con los totales y líneas divisorias
    table = PrettyTable()
    # Columnas: Misión + Tipos de Dispositivo
    missions = sorted(set(mission for _, mission, _ in total_count_by_device_mission_state if mission != "UNKN"))
    device_types = sorted(set(device for device, _, _ in total_count_by_device_mission_state))
    table.field_names = ["Dispositivo / Estado", *missions, "Total"]

    # Filas: Tipos de Dispositivo + Estados
    for device_type in device_types:
        for state in ["excelente", "bueno", "advertencia", "defectuoso", "inoperable", "desconocido"]:
            row = [f"{device_type} - {state}"]
            for mission in missions:
                # Obtener la cantidad total para la combinación de Tipo de Dispositivo, Misión y Estado
                total_count = total_count_by_device_mission_state.get((device_type, mission, state), 0)
                row.append(total_count)
            # Sumar los totales por Estado
            state_total = sum(row[1:])
            row.append(state_total)
            table.add_row(row)
        # Línea divisoria después de cada grupo de dispositivo
        table.add_row(["-" * 20] * (len(missions) + 2))

    # Filas: Totales por Misión
    total_row = ["Total"]
    for mission in missions:
        mission_total = sum(total_count_by_device_mission_state.get((device_type, mission, state), 0)
                            for device_type in device_types
                            for state
                            in ["excelente", "bueno", "advertencia", "defectuoso", "inoperable", "desconocido"])
        total_row.append(mission_total)
    total_row.append(sum(total_row[1:]))
    table.add_row(total_row)

    return str(table)


@table_decorator("Tabla 2: Dispositivos con mayor número de desconexiones 'desconocido' para cada misión")
def gudt(state_count: Dict):  # generate_unknown_disconnects_table
    """ @Juliana falta aquí un mejor docstring
    """
    # Obtener la lista única de misiones, tipos de dispositivo y estados
    missions = sorted(set(mission for mission, _, _ in state_count.keys()))
    device_types = sorted(set(device for _, device, _ in state_count.keys()))

    table = PrettyTable()

    # Configurar los nombres de las columnas
    table.field_names = ["Misión", "Tipo de Dispositivo", "Desconexiones 'desconocido'"]

    # Ordenar las misiones alfabéticamente
    sorted_missions = sorted(missions)

    # Agregar filas para cada Misión, Tipo de Dispositivo y Estado 'desconocido'
    for mission in sorted_missions:
        for device in device_types:
            desconocido_count = state_count.get((mission, device, "desconocido"), 0)

            # Verificar si hay desconexiones antes de agregar la fila a la tabla
            if desconocido_count > 0:
                table.add_row([mission, device, desconocido_count])

    return str(table)


@table_decorator("Tabla 3: Porcentaje de datos generados para cada dispositivo y misión")
def gpt(total_events: Dict, logs: List[DeviceLog]):  # generate_percentage_table
    """ @Juliana falta aquí un mejor docstring
    """
    table = PrettyTable()
    table.field_names = ["Misión", "Tipo de Dispositivo", "Porcentaje de Datos"]

    # Obtener misiones únicas y ordenarlas alfabéticamente
    missions = sorted(set(key[0] for key in total_events.keys()))

    for mission in missions:
        for key, count in total_events.items():
            # Filtrar por misión y calcular el porcentaje
            if key[0] == mission:
                percentage = (count / len(logs)) * 100
                table.add_row([key[0], key[1], f"{percentage:.2f}%"])

    return str(table)


@table_decorator("Tabla 4: Consolidado de todas las misiones para determinar cuántos dispositivos son inoperables")
def gidt(total_events: Dict, state_count: Dict):  # generate_inoperable_devices_table
    """ @Juliana falta aquí un mejor docstring
    """
    table = PrettyTable()
    table.field_names = ["Misión", "Tipo de Dispositivo", "Dispositivos Inoperables"]

    # Filtrar las misiones con 0 dispositivos inoperables
    filtered_missions = {key[0] for key in total_events.keys()
                         if state_count.get((key[0], key[1], "inoperable"), 0) > 0}

    # Ordenar las misiones alfabéticamente
    sorted_missions = sorted(filtered_missions)

    for mission in sorted_missions:
        for key, count in state_count.items():
            # Filtrar solo los dispositivos inoperables
            if key[0] == mission and key[2] == "inoperable" and count > 0:
                table.add_row([key[0], key[1], count])

    return str(table)


def save_report_to_file(report_content: str, report_name: str, reports: Path) -> None:
    """ @Juliana falta aquí un mejor docstring
    """
    try:
        report_path = reports / report_name
        with open(report_path, "w") as report_file:  # @Juliana, aquí pide usar encoding, pero no supe dar con cual
            report_file.write(report_content)
        print(f"El informe se ha guardado en: {report_path}")
    except IOError as e:  # @Juliana mejoré el Exception para que no fuera tan amplio, no sé si sea el mejor
        print(f"Error al guardar el informe: {str(e)}")
        raise  # Agregamos esta línea para que el error se propague y se muestre en la consola


def process_logs(logs: List[DeviceLog], reports: Path) -> bool:
    """ @Juliana falta aquí un mejor docstring
    """
    sta_cou = {}  # state_count
    tot_eve = {}  # total_events

    try:
        if not logs:
            raise ValueError("No se encontraron archivos de registro para procesar.")

        for log in logs:
            # print(f"Procesando log: {log}") @Juliana se comenta ya que no se requiere en la ejecución final
            state_key = (log.mision, log.tipo_dispositivo, log.estado_dispositivo)
            sta_cou[state_key] = sta_cou.get(state_key, 0) + 1

            total_events_key = (log.mision, log.tipo_dispositivo)
            tot_eve[total_events_key] = tot_eve.get(total_events_key, 0) + 1

        report_content: str = (gsct(sta_cou) + gudt(sta_cou) + gpt(tot_eve, logs) + gidt(tot_eve, sta_cou))

        print("Contenido del informe:")
        print(report_content)

        report_name = f"APLSTATS-REPORTE-{logs[0].fecha}.log"
        save_report_to_file(report_content, report_name, reports)

        return True  # Indicador de éxito

    except ValueError as e:  # @Juliana mejoré el Exception para que no fuera tan amplio, no sé si sea el mejor
        print(f"Error al procesar los logs: {str(e)}")
        return False  # Indicador de fallo
