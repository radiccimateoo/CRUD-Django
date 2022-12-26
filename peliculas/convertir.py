import base64

def conversion(archivo):
    imagen = open('c:/Users/SONY VAIO/Desktop/nuevo_desafio/proyecto/peliculas/static/img/' + archivo, 'rb')
    convertida = base64.b64encode(imagen.read())
    imagen.close()

    return convertida