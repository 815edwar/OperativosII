# Operativos II

# Proyecto I - Simulador de despachador de procesos linux

En este proyecto se trabajo en una simulacion general del comportamiento de un despachador de procesos
en el SO Linux que utiliza el algoritmo CFS para el despacho.

Para correr el proyecto es necesario el siguiente comando:

    $ ./main.py [--cpu-slices value] [--cores-quantity value] [--proc-gen-interval value] [--speed value]

    Donde:

    - El valor de cpu-slices es un numero con el quantum que tendran los cpu de la simulacion
    - El valor de cores-quantity es un numero con el numero de cores que tendra la simulacion
    - El valor de proc-gen-interval es un numero con el intervalo en unidades de tiempo del simulador en el que se generan procesos
    - El valor de speed es un string con la velocidad en la que quiere que se corra el simulador. Las opciones son:
      1.- rapida: Donde 1 unidad de tiempo del simulador equivale a 1 segundo
      2.- normal: Donde 1 unidad de tiempo del simulador equivale a 3 segundos
      3.- lenta: Donde 1 unidad de tiempo del simulador equivale a 5 segundos