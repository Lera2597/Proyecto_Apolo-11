""" 
Genera un informe consolidado a partir de los registros de dispositivos y lo guarda en el directorio de informes.
"""

from pathlib import Path
from apolo_11.src.reportes.reportes import extract_logs_from_folder, process_logs


def consolidado(devices: str, reports: str) -> None:
    """
    Genera un informe consolidado a partir de los registros de dispositivos y lo guarda en el directorio de informes.

    Este informe consolidado contiene estadísticas sobre los eventos registrados en los dispositivos, 
    incluyendo la cantidad total de eventos por estado para cada misión y dispositivo, dispositivos con 
    mayor número de desconexiones 'desconocido' para cada misión, porcentaje de datos generados para cada 
    dispositivo y misión, y el consolidado de todas las misiones para determinar cuántos dispositivos son inoperables.

    :param devices: Ruta del directorio que contiene los archivos de registro de dispositivos.
    :type devices: str
    :param reports: Ruta del directorio donde se guardarán los informes generados.
    :type reports: str
    :return: None
    """
    directorio_devices = Path(devices)  
    directorio_reports = Path(reports)
    directorio_reports.mkdir(exist_ok=True)
    logs_list = extract_logs_from_folder(directorio_devices)
    process_logs(logs_list, directorio_reports)
