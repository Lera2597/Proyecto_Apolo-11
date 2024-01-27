# Proyecto Apolo-11

Apolo-11 es un programa desarrollado en Python que simula y consolida registros generados por diferentes componentes de misiones espaciales. Su objetivo principal es proporcionar una herramienta flexible y eficiente para la generación y gestión de archivos de registro (.log) simulados, que contienen información semiestructurada sobre diversas misiones, dispositivos y estados de dispositivos.

## Tabla de Contenido

- [Resumen](#resumen)
- [Instalación](##instalación)
- [Uso](##uso)
- [Recursos](##recursos)
- [Créditos](##créditos)
- [Licencia](##licencia)

## Resumen 

El programa Apolo-11 permite simular la creación de archivos .log de forma aleatoria para múltiples misiones, cada una con un conjunto variado de dispositivos y estados de dispositivos. Utiliza una estructura modular para gestionar diferentes aspectos de la simulación, como la generación de datos, la configuración de archivos, la creación de archivos .log y la generación de reportes de ejecución.

Algunas características clave del proyecto incluyen:

* **Simulación de Misiones Espaciales:** El programa simula la creación de archivos .log para misiones espaciales específicas, generando datos aleatorios para diferentes tipos de dispositivos y estados de dispositivos.

* **Configuración Personalizable:** Los usuarios pueden ajustar la configuración del programa, como el rango de cantidad de archivos generados en cada ejecución, el tiempo de la ejecución y otros parámetros relevantes.

* **Generación de Informes:** El programa genera informes de ejecución que resumen la información clave sobre cada simulación realizada, proporcionando una visión general de los archivos .log generados y su contenido.

## Instalación

Para instalar y ejecutar el Proyecto Apolo-11, sigue estos pasos:

1. Clonar el repositorio:

Clona este repositorio en tu máquina local utilizando Git:

```bash
git clone https://github.com/Lera2597/Proyecto_Apolo-11
```

2. Instalar las dependencias:

Este proyecto utiliza Poetry para la gestión de dependencias. Asegúrate de tener Poetry instalado en tu sistema. Luego, desde la raíz del proyecto, ejecuta:

```bash
cd Proyecto_Apolo-11
poetry install
```

3. Ejecución 

Una vez completados los pasos anteriores, puedes ejecutar el programa con el siguiente comando:

```bash
poetry run python apolo_11.py conf.yaml
```
Esto iniciará el programa Apolo-11 y te mostrará el menú inicial con las opciones disponibles.

## Uso

El programa Apolo-11 ofrece varias funcionalidades que se pueden acceder desde un menú principal. A continuación se muestran algunos ejemplos de cómo utilizar estas funcionalidades:

![image](https://github.com/Lera2597/Proyecto_Apolo-11/assets/77032671/7fc56942-d704-4bb9-adec-cdc4e17c6a72)


**Ejecutar Simulación**

Para ejecutar la simulación y generar archivos .log con información aleatoria para las misiones espaciales, sigue estos pasos:

1. Ejecuta el programa.
2. Selecciona la opción "Ejecutar simulación" desde el menú principal presionando la letra `E` desde tu teclado.
3. Espera a que termine la ejecución para decidir qué más hacer.

**Consultar Simulaciones**

Puedes consultar la información generada en las simulaciones anteriores utilizando la opción "Consultar simulaciones" en el menú principal presionando la letra `C` desde tu teclado. Esta función te permitirá ver los reportes de las misiones espaciales.

**Modificar Archivo de Configuración**

Si deseas ajustar la configuración del programa, puedes seleccionar la opción "Modificar archivo de configuración" desde el menú principal presionando la letra `M` desde tu teclado. Esto te permitirá cambiar los parámetros de la simulación, como el número de registros a generar, el tiempo de la simulación, etc.

**Salir del Programa**

Para salir del programa, simplemente selecciona la opción "Salir del programa" desde el menú principal presionando la letra `S` desde tu teclado. Esto cerrará el programa y te devolverá al sistema operativo.

## Recursos

Explora algunos de los recursos y archivos que desarrollamos para entender la asignación, planificar las tareas y diseñar la solución:

1. **Tablero de Trello:** Revisa nuestro tablero de [Trello](https://trello.com/b/KamrOQ1V/apolo-11) para ver las historias de usuario, criterios de aceptación y planificación del proyecto.

2. **Diagrama conceptual:** Consulta el diagrama que muestra el [concepto general](https://docs.google.com/presentation/d/13GVTztkxqtjyj7kFPzNF9TqsN7h0cHyU/edit?usp=sharing&ouid=104613954867366461524&rtpof=true&sd=true) del programa.

3. **Diseño del producto:** Accede a nuestro archivo que detalla el [diseño de la solución](https://docs.google.com/spreadsheets/d/1cgXblJoMPm_Rkvatb3BZSA0NWqjRvP1i4lkoV5-q4_A/edit?usp=sharing), incluyendo sus módulos y funcionalidades.

4. **Flujograma del sistema:** Revisa el [flujograma](https://drive.google.com/file/d/1Gu_BSi945BUNluNzpqJBZHE6Sf2vWyL-/view?usp=sharing) que representa visualmente el programa y sus procesos.

## Créditos

Este proyecto fue posible gracias al esfuerzo conjunto y la colaboración de los siguientes miembros del equipo:

- Luis Eduardo Rodríguez Ascuntar [<img src="https://img.icons8.com/fluency/23/null/linkedin.png"/>](https://www.linkedin.com/in/luis-eduardo-rodriguez-ascuntar/)
- César Augusto Chacón Silva [<img src="https://img.icons8.com/fluency/23/null/linkedin.png"/>](https://www.linkedin.com/in/cesarachs/)
- Juliana Andrea Amézquita Abello [<img src="https://img.icons8.com/fluency/23/null/linkedin.png"/>](https://www.linkedin.com/in/julianaamezquita/)

Agradecemos al profesor Luis Fernando Vásquez Vergara por su tiempo, dedicación y orientación durante el [Bootcamp Coding Up My Future](https://github.com/codingupmyfuture/bootcamplinuxpython).

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).
