from django.shortcuts import render, HttpResponse

# Create your views here.
menu = """
"""

def principal(request):
    contenido=""
    # return HttpResponse(menu +contenido)
    return render(request,"inicio/principal.html")

def contacto(request):
    contenido=""""""
    #return HttpResponse(contenido)
    return render(request,"inicio/contacto.html")

def formulario(request):
    contenido = """
       """
    #return HttpResponse(contenido)
    return render(request,"inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")