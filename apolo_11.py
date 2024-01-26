"""Main que invoca a la simulación en caso de que se quiera ejecutar basada en la lógica desarrollada
"""

from argparse import ArgumentParser as ap
from argparse import Namespace
from pathlib import Path
from apolo_11.src.menu.cli_control import while_menu


def main(nombre: str) -> None:
    """
    Función principal encargada de la invocación al menú inicial de la aplicación.
    """
    try:
        dir_conf: Path = Path("apolo_11/config")
        dir_compl: Path = dir_conf / nombre
        with dir_compl.open("r", encoding="utf8") as file:
            contenido: str = file.read()
        while_menu(contenido, "menu_principal")
    except FileNotFoundError:
        print("El archivo de configuración no se encuentra en la ruta.")


if __name__ == "__main__":
    parser = ap(description="Encargado de la invocación del menú del programa")
    parser.add_argument("archivo", help="Nombre del archivo (.yml) de configuración para la simulación")
    args: Namespace = parser.parse_args()
    main(args.archivo)
