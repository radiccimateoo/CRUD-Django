import base64

def conversion():
    imagen = open('base.jpg', 'rb')
    leer = base64.b64encode(imagen.read())
    imagen.close()

    return leer