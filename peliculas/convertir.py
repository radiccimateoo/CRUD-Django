import base64

def conversion(archivo):
    imagen = open(archivo, 'rb')
    convertida = base64.b64encode(imagen.read())
    imagen.close()

    return convertida