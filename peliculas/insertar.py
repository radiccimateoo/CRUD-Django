import datetime

def insertar(registro):
    archivo = open('insertBDD.txt', 'a')

    fecha_hora = datetime.datetime.now()
    dato_final = archivo.write(str(fecha_hora) + '\n' + str(registro) + '\n')

    archivo.close()

    return dato_final

def leer():

    archivo = open('insertBDD.txt', 'r')
    lectura = archivo.readlines()
    archivo.close()

    return lectura
