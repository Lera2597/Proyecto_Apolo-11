""" Contiene las funcionalidades para el control de los menús y sus llamados dentro de la aplicación
"""

from os import system, name
from pathlib import Path
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
    clean_screen()

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


def e_function(path_salida: str, path_backup: str, path_report: str) -> None:
    """ Controla la invocación a la ejecución de la simulación

    :param path_salida: Directorio donde se escriben los archivos .log
    :type path_salida: str
    :param path_backup: Directorio donde se respaldan los archivos .log
    :type path_backup: str
    :param path_report: Directorio donde se guardan los reportes de ejecución
    :type path_report: str
    """
    clean_screen()
    dgi(path_salida)
    sleep(2)

    clean_screen()
    con(path_salida, path_report)
    input("Finalizó el reporte, presione cualquier tecla para continuar...")

    rcs(path_salida, path_backup)


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
    """ Controla los menús y el llamado a las invocación de funciones

    :param archivo: Contiene el contenido del archivo menu.yaml para que se puedan tomar las
    variables que lo conforman
    :type archivo: str
    :param menu: Indica cual es el título del menú que se desea imprimir
    :type menu: str
    """
    conf: dict = safe_load(archivo)

    control: bool = True
    while control:
        print_menu(conf, menu)
        select: str = input(f"{conf['pantalla']['option']}").upper()
        options: list = [option["desc"] for option in conf[menu]["opciones"]]
        functions: list = [option["func"] for option in conf[menu]["opciones"]]
        cont: int = 0

        for option in options:
            if option[0].upper() == select:
                control = invocar_funciones(functions, archivo, cont, conf, control)
                break
            cont += 1

        if cont == len(options) and control:
            print(f"{conf['pantalla']['mistake']}")
            sleep(1)


def invocar_funciones(functions: list, archivo: str, cont: int, conf: dict, control: bool) -> bool:
    """Controla las funciones que deben ser llamadas dependiendo de lo decidido en el menú

    :param functions: Listas de las funciones disponibles dependiendo del menú utilizado
    :type functions: list
    :param archivo: Contiene el contenido del archivo de configuraciones del programa
    :type archivo: str
    :param cont: Controla el contador que decide en que funcione se ingresó en el menú
    :type cont: int
    :param conf: Tiene el contenido del archivo convertido en diccionario para su selección
    :type conf: dict
    :param control: Contiene el valor que indican si se debe volver o salir del programa
    :type control: bool
    :return: Retorna un estado distinto al indicado en el parametro de control en caso de ser necesario
    :rtype: bool
    """
    call: Callable = globals()[functions[cont]]
    if functions[cont] == "while_menu":
        valores: list = [archivo, "menu_consulta"]
        call(*valores)
    elif functions[cont] == "s_function":
        valores: str = [conf["pantalla"]["mistake"]]
        if call(*valores):
            control = False
    elif functions[cont] == "e_function":
        valores: list = [conf["directorio_salida"], conf["directorio_backup"], conf["directorio_report"]]
        call(*valores)
    elif (functions[cont] == "u_function" or functions[cont] == "e_c_function"):
        valores: list = [conf["directorio_report"]]
        call(*valores)
    else:
        if call():
            control = False
    return control


def u_function(path_report: str) -> None:
    """ Controla la búsqueda de la última ejecución de la simulación

    :param path_report: Directorio donde se guardan los reportes de ejecución
    :type path_report: str
    """
    clean_screen()
    directorio = Path(path_report)
    ext_archivo = ".log"
    archivos = list(directorio.glob(f'*{ext_archivo}'))

    if archivos:
        archivo_mas_reciente: Path = max(archivos, key=lambda archivo: archivo.stat().st_mtime)
        with archivo_mas_reciente.open("r") as archivo:
            contenido: str = archivo.read()
        print(f"Contenido del informe: {archivo_mas_reciente.name}\n")
        print(contenido)
        input("Presione cualquier tecla para continuar...")
    else:
        print("No hay archivos en el directorio.")
        sleep(2)


def e_c_function(path_report: str) -> None:
    """ Controla la búsqueda de la última ejecución de la simulación

    :param path_report: Directorio donde se guardan los reportes de ejecución
    :type path_report: str
    """
    clean_screen()
    directorio = Path(path_report)
    ext_archivo = "*.log"
    archivos = list(directorio.glob(f'{ext_archivo}'))
    if archivos:
        print("Reportes encontrados:")
        for archivo in archivos:
            print(f"> {archivo.name}")
        nombre_buscar: str = input("Indique el nombre del archivo a buscar: ")
        archivo_buscar: Path = directorio / nombre_buscar
        clean_screen()
        if archivo_buscar in archivos:
            with archivo_buscar.open("r") as archivo:
                contenido: str = archivo.read()
            print(f"Contenido del informe: {archivo_buscar.name}\n")
            print(contenido)
            input("Presione cualquier tecla para continuar...")
        else:
            print(f'El archivo "{archivo_buscar.name}" no se encuentra en el directorio.')
            input("Presione cualquier tecla para continuar...")
    else:
        print("No hay archivos en el directorio.")
        sleep(2)


def r_function() -> bool:
    """ Controla el regreso al menú anterior

    :return: Devuelve true para regresar al menú anterior y deja espacio para usarse en otros menús
    :rtype: bool
    """
    return True


def clean_screen() -> None:
    """ Limpia la pantalla dependiendo del sistema operativo
    """
    system("cls" if name == "nt" else "clear")
