from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

def generar_pdf(template, contexto={}):

    # obtener o recuperar el template que vamos a pasar a PDF
    obtener_template = get_template(template) 

    # al template que recuperamos le pasamos el contexto
    pasar_contexto = obtener_template.render(contexto) 

    # mediante pisaDocument transformamos a archivo PDF, pero este metodo necesita ser encodeado mediante un
    # conjunto de de bytes que sea compatible con PDF, para eso usamos BytesIO del modulo io
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(pasar_contexto.encode('ISO-8859-1')), result)

    # mediante una condicion podemos evaluar si no hay errores para que me devuelva el docuemnto PDF
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='aplication/pdf')