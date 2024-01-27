"""
Main que invoca a la simulación en caso de que se quiera ejecutar basada en nuestra lógica.
"""
from apolo_11.src.menu.cli_control import while_menu
from pathlib import Path

def main() -> None:
    """
    Función principal encargada de la invocación al menú inicial de la aplicación.
    """
    try:
        file_path:str = Path("Proyecto_Apolo-11","apolo_11","config","menu.yaml")
        print(file_path)
        with open(file_path, "r", encoding="utf8") as file:
            contenido = file.read()
        while_menu(contenido, "menu_principal")
        #data_generator_init()
    except FileNotFoundError:
        print("El archivo de configuración no se encuentra en la ruta.")

if __name__ == "__main__":
    main()
