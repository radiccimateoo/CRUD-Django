import datetime

def insertar(registro):
    archivo = open('insertBDD.txt', 'a')

    d = datetime.datetime.now()
    fecha = str(d.day) + '/' + str(d.month) + '/' + str(d.year)
    hora = str(d.hour) + ':' + str(d.minute) + ':' + str(d.second)

    actual = [fecha + '--' + hora]

    dato_final = archivo.write(str(actual) + '\t' + str(registro) + '\n')

    archivo.close()

    return dato_final

def leer():

    archivo = open('insertBDD.txt', 'r')
    lectura = archivo.readlines()
    archivo.close()

    return lectura
