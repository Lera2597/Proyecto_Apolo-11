""""
Main que invoca a la simulación en caso de que se quiera ejecutar basada en nuestra lógica.
"""

from apolo_11.src.menu.cli_control import while_menu

def main() -> None:
    """
    Función principal encargada de la invocación al menú inicial de la aplicación.
    """
    try:
        with open("apolo_11//config//menu.yaml", "r", encoding="utf8") as file:
            contenido = file.read()
        while_menu(contenido, "menu_principal")
    except FileNotFoundError:
        print("El archivo de configuración no se encuentra en la ruta.")

if __name__ == "__main__":
    main()
