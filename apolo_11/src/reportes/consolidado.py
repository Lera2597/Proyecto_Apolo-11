import argparse
from pathlib import Path
from apolo_11.src.reportes.reportes import extract_logs_from_folder, process_logs

def consolidado():
    parser = argparse.ArgumentParser(description="Procesa archivos de registro y genera informes en archivos .log.")
    parser.add_argument("folder_path", type=Path, default="devices", help="Ruta a la carpeta que contiene los archivos de registro.")
    parser.add_argument("--reports_folder", type=Path, default="reports", help="Ruta a la carpeta para almacenar los informes.")
    args = parser.parse_args()

    args.reports_folder.mkdir(exist_ok=True)  # Crear la carpeta de informes si no existe
    logs_list = extract_logs_from_folder(args.folder_path)
    process_logs(logs_list, args.reports_folder)