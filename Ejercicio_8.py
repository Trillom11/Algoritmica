'''8. Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar'''

from xml.etree import ElementInclude
from Class_colas_prioridad import *
import os
os.system('clear')
miMonticulo = ColaPrioridad()

def elegir_opcion():
    print('\n\n\t***ELIGE UNA OPCIÓN***')
    print('\tPulsa 1 si quieres introducir un valor.')
    print('\tPulsa 2 si quieres introducir un montículo de valores.')
    print('\tPulsa 3 si quieres verificar si la lista está vacía.')
    print('\tPulsa 4 si quieres verificar el máximo del montículo')
    print('\tPulsa 5 si quieres extraer el valor máximo del montículo')
    print('\tPulsa 6 si quieres extraer el valor mínimo del montículo')
    print('\tPulsa 7 si quieres recorrer la lista.')
    try:
        opcion=int(input('\t'))
        
        while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6 and opcion!=7:
            opcion=elegir_opcion()

        return opcion
    except:
        main()

def repetir():
    Y_N=input('\n\n\t¿Deseas ejecutar de nuevo el programa?(Y/N): ')
    Y_N=Y_N.lower()

    while Y_N!='y' and Y_N!='n':
        print('\n***Has cometido un error, inténtalo de nuevo.***\n ')
        Y_N=input('\n\n\t¿Deseas ejecutar de nuevo el programa?(Y/N): ')
        Y_N=Y_N.lower()

    if  Y_N=='y':
        main()
    
    if Y_N=='n':
        print('\n***Gracias por ejecutar el programa.***')
        exit(0)

def vacio():
    vacia=miMonticulo.esta_Vacia()
    if vacia:
        print('La lista está vacía.')
        main()

def main():
    opcion=elegir_opcion()

    print('\n\n','-'*40)
    if opcion==1:
        try:
            valor=int(input('\nIntroduce el valor a añadir en el montículo:\n'))
            miMonticulo.agregar(valor)
            repetir()
        except:
            print('\nHas cometido un error, inténtalo de nuevo.')
            main()
 
    if opcion==2:
        try:
            valor=input('\nIntroduce los valores a añadir en el montículo separados por comas:\n')
            valor=valor.split(',')
            valor=[int(v) for v in valor]
            miMonticulo.construirMonticulo(valor)
            repetir()
        except:
            print('\nHas cometido un error, inténtalo de nuevo.')
            main()

    if opcion==3:
        vacia=miMonticulo.esta_Vacia()
        if vacia:
            print('La lista está vacía.\n')
        else:
            print('La lista tiene valores dentro.')
        repetir()

    if opcion==4:
        vacio()
        print('El valor máximo de la lista es: ',miMonticulo.maximo())
        repetir()

    if opcion==5:
        vacio()
        print('El valor máximo de la lista es: ',miMonticulo.extrae_y_borra(), ' el cuál acaba de ser eliminado.')
        repetir()

    if opcion==6:
        vacio()
        print('El valor mínimo de la lista es: ',miMonticulo.eliminarMin(), ' el cuál acaba de ser eliminado.')
        repetir()

    if opcion==7:
        print('La lista en un recorrido preorden, avanzando y dejando atrás el valor más pequeño es:')
        miMonticulo.avanzar()
        repetir()

main()