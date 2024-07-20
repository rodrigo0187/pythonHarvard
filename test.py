import random
from statistics import median
from math import isnan
from itertools import filterfalse
import csv
import os
import sys


m = '-'*35

nombres = ["Ana", "Luis", "Carlos", "Maria", "Pedro",
           "Laura", "Juan", "Sofia", "Jose", "Marta"]

# diccionario de sueldos
sueldos = {nombre: random.randint(300000, 2500000) for nombre in nombres}
lista = []
head = ["ID_Empleado", "Nombre Empleado", "Sueldo Empleado"]
ruta = r"csv\\registro.csv"


def asignar_sueldos():
    print('Lista de los Empleados')
    for i, nombre in enumerate(nombres, start=1):
        print(f'{i} {nombre}')
    # asignar sueldo a los empleados
        sueldo_nuevo = random.randint(300000, 2500000)
        sueldos[nombre] = sueldo_nuevo
        random.randint(1, 100)

        diccEmpleado = {
            "ID_Empleado": random.randint(1, 100),
            "Nombre Empleado": nombre,
            "Sueldo Empleado": sueldo_nuevo
        }

    # creaamos la lista
        lista.append(diccEmpleado)

    # ordenar con sorted y utilizar lambda
        diccEmpleado = sorted(lista, key=lambda x: x["Sueldo Empleado"])

    # recorrer lista
    print("Sueldos agregados correctamente")
    print('-'*30)
    employe = [(row["ID_Empleado"], row["Nombre Empleado"], row["Sueldo Empleado"])
               for row in lista]

    print(f'{employe}')
    print('-'*30)


def grabar():
    ruta = r"D:\WorkSpace\pythonHarvard\registro.csv"
    # directory = os.path.dirname(ruta)
    if not os.path.isfile(ruta):
        print('El archivo no existe en la ruta')
        print('-'*35)
        crear = input('Desea crear el archivo? S/N: ')
        if crear.lower() != 's':
            return
        try:
            # verfico si el archivo existe y verfica si tiene permiso de escritura
            if os.path.exists(ruta) and os.access(ruta, os.W_OK):
                with open(ruta, 'w')as f:
                    f.write('Datos a escribir en el archivo CSV\n')
        except IOError:
            print()
            print(f'no se puede escribir el archivo de ruta {ruta}')
            print()
            return
        else:
            print(f'archivo creado con exito')
            print('-'*35)
        try:
            with open(ruta, 'w', newline='') as recordFile:
                writer = csv.DictWriter(
                    recordFile, dialect='excel', fieldnames=head)
                writer.writeheader()
                writer.writerows(lista)
        except IOError:
            print()
            print(f'no se puede escribir el archivo de ruta {ruta}')
            print()


def listarEmpleados():
    os.system('cls')
    # comprobar si existe el archivo
    ruta = r'D:\WorkSpace\pythonHarvard\registro.csv'
    if not os.path.isfile(ruta):
        print(f'el archivo no existe o no es un archivo regular {ruta}')

    if not os.access(ruta, os.R_OK):
        print('El archivo no se puede leer')
        print()
    if not os.path.exists(ruta):
        print(f'el archivo no existe: {ruta}')
        print()
    else:
        try:
            with open(ruta, 'r', newline='') as listEmpleados:
                reader = csv.DictReader(
                    listEmpleados, fieldnames=head, dialect='excel', delimiter=',')

                empleados = [(row['ID_Empleado'], row['Nombre Empleado'], row['Sueldo Empleado'])
                             for row in reader]
                if not empleados:
                    print('no existe listado de empleados')
                    return False
                print(m)
                print('Listado de Empleados')
                print(m)
                for empleado in empleados:
                    print(f'{empleado[0]}, {empleado[1]}, {empleado[2]}')
            print(m)
            enter = input('Presiones enter para continuar.....')
            os.system('cls')
        except ValueError as e:
            print(f'Error: {e}')


def buscarEmpleado():
    # verficar si existe el archivo y validar si tiene ejecucion
    os.system('cls')
    ruta = r'D:\WorkSpace\pythonHarvard\registro.csv'

    if not os.path.exists(ruta):
        print('El archivo no existe.')
        return False
    if not os.access(ruta, os.R_OK):
        print('El archivo no tiene permisos de lectura.')
        return False

    print('Busca Empleado por (Nombre o ID)')
    options = {
        1: "Nombre",
        2: "ID",
        3: "Menu"
    }

    while True:
        for clave, valor in options.items():
            print(f'{clave}. {valor}')

        try:
            op = int(input('Ingrese una de las opciones: '))
        except ValueError:
            print('Opción no válida. Por favor ingrese un número.')
            continue

        if op not in options:
            print('Opción no válida')
            continue

        with open(ruta, 'r', newline='') as buscarCSV:
            reader = csv.DictReader(buscarCSV)

            if op == 1:
                findEmploye = input(
                    'Ingrese el nombre del empleado: ').capitalize()
                encontrado = False

                for row in reader:
                    if row['Nombre Empleado'].capitalize() == findEmploye:
                        print(f'Empleado encontrado: {findEmploye}')
                        print(f"{row['ID_Empleado']}, {
                              row['Nombre Empleado']}, {row['Sueldo Empleado']}")
                        encontrado = True

                if not encontrado:
                    print('Nombre no encontrado')

            elif op == 2:
                try:
                    findIDemploye = int(
                        input('Ingrese el ID del empleado: '))
                except ValueError:
                    print('ID no válido. Por favor ingrese un número.')
                    continue

                encontrado = False

                for row in reader:
                    if int(row['ID_Empleado']) == findIDemploye:
                        print(f'El ID {findIDemploye} ha sido encontrado')
                        print(f"{row['ID_Empleado']}, {
                              row['Nombre Empleado']}, {row['Sueldo Empleado']}")
                        encontrado = True

                if not encontrado:
                    print('ID no encontrado en la base de datos')

            elif op == 3:
                break

        input('Presione Enter para continuar')


def menu():
    # clave y valor
    opciones = {
        1: "asignar sueldo",
        2: "Grabar",
        3: "listar",
        4: "Buscar",
        5: "Salir"
    }
    while True:
        try:
            for clave, valor in opciones.items():
                print(f'{clave}. {valor}')
            print(m)
            op = int(input('Ingrese una de las opciones: '))
            if op not in opciones:
                print(m)
                print(f'Ingrese una de las opciones {opciones}')
                print(m)
                continue
            else:
                if op not in [1, 2, 3, 4, 5]:
                    print('opcion no valida')
                    continue
                if op == 1:
                    asignar_sueldos()
                if op == 2:
                    grabar()
                if op == 3:
                    listarEmpleados()
                if op == 4:
                    buscarEmpleado()
                if op == 5:
                    sys.exit()
                print(f'{opciones[op]} (Seleccionado)')
        except (TypeError, ValueError) as t:
            print(m)
            print(f'Error: {t}')
            print(m)


if __name__ == '__main__':
    while True:
        menu()
