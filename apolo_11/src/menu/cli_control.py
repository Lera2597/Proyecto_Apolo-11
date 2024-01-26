""" Contiene las funcionalidades para el control de los menús y sus llamados dentro de la aplicación
"""

from os import system, name
from time import sleep
from typing import Callable
from yaml import safe_load
from apolo_11.src.datos.data_generator import data_generator_init as dgi
from apolo_11.src.archivos.gestor import realizar_copia_seguridad as rcs
from apolo_11.src.reportes.consolidado import consolidado as con


def print_menu(configuracion: dict, menu: str) -> None:
    """ Imprime el menú de la aplicación o de las consultas

    :param configuracion: Contiene la información con la configuración de las variables de trabajo
    :type configuracion: dict
    :param menu: Indica cual es el título del menú que se desea imprimir
    :type menu: str
    """
    system("cls" if name == "nt" else "clear")

    options: list = [option["desc"] for option in configuracion[menu]["opciones"]]
    des_men: str = configuracion[menu]["cabecera"]
    max_lon: int = max(len(option) for option in options)
    if max_lon < configuracion["pantalla"]["size"]:
        max_lon = configuracion["pantalla"]["size"]
    des_men_lon: int = max(len(des_men), max_lon)
    char: str = configuracion["pantalla"]["print"]
    if len(char) > 1:
        char = char[:1]

    print(f"{char}" * (des_men_lon + 2))
    print(f"{char}{des_men.center(des_men_lon)}{char}")
    print(f"{char}" * (des_men_lon + 2))
    for option in options:
        print(f"{char}{option.center(max_lon)}{char}")
    print(f"{char}" * (des_men_lon + 2))


def e_function() -> None:
    """ Controla la invocación a la ejecución de la simulación
    """
    system("cls" if name == "nt" else "clear")
    dgi()
    sleep(2)

    system("cls" if name == "nt" else "clear")
    con()
    input("Finalizó el reporte, presiona Enter para continuar...")

    system("cls" if name == "nt" else "clear")
    rcs("devices")
    input("Finalizó backup, presiona Enter para continuar...")


def m_function() -> None:
    """ Controla la invocación a la modificación del archivo de configuración
    """
    print("Ir a modificar")
    sleep(1)


def s_function(texto: str) -> bool:
    """ Controla la salida del programa

    :param texto: Contiene el texto que se muestra en caso de que se ingrese un valor incorrecto
    :type texto: str
    :return: Devuelve true en caso de que se deba salir y false en caso contrario
    :rtype: bool
    """
    select: str = input("¿Desea salir del programa? (S/N) ").upper()

    if select == "S":
        return True
    if select == "N":
        return False
    print(texto)
    sleep(1)
    return False


def while_menu(archivo: str, menu: str) -> None:
    """ Controla los menús y sus invocaciones hasta que se cierre el programa

    :param archivo: Contiene el contenido del archivo menu.yaml para que se puedan tomar las
    variables que lo conforman
    :type archivo: str
    :param menu: Indica cual es el título del menú que se desea imprimir
    :type menu: str
    """
    conf_menu: dict = safe_load(archivo)

    control: bool = True
    while control:
        print_menu(conf_menu, menu)
        select: str = input(f"{conf_menu['pantalla']['option']}").upper()
        options: list = [option["desc"] for option in conf_menu[menu]["opciones"]]
        functions: list = [option["func"] for option in conf_menu[menu]["opciones"]]
        cont: int = 0

        for option in options:
            if option[0].upper() == select:
                call: Callable = globals()[functions[cont]]
                if functions[cont] == "while_menu":
                    valores: list = [archivo, "menu_consulta"]
                    call(*valores)
                elif functions[cont] == "s_function":
                    valores: str = [conf_menu["pantalla"]["mistake"]]
                    if call(*valores):
                        control = False
                else:
                    if call():
                        control = False
                break
            cont += 1

        if cont == len(options) and control:
            print(f"{conf_menu['pantalla']['mistake']}")
            sleep(1)


def u_function() -> None:
    """ Controla la búsqueda de la última ejecución de la simulación
    """
    print("Ir a última")
    sleep(1)


def e_c_function() -> None:
    """ Controla la búsqueda de una ejecución específica
    """
    print("Ir a específica")
    sleep(1)


def t_function() -> None:
    """ Controla la búsqueda de los totales del programa
    """
    print("Ir a totales")
    sleep(1)


def r_function() -> bool:
    """ Controla el regreso al menú anterior

    :return: Devuelve true en caso de que se deba salir y false en caso contrario
    :rtype: bool
    """
    print("Regresando al menú anterior")
    sleep(1)
    return True
