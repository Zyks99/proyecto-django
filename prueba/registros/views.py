from django.shortcuts import render,redirect
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages
from .models import Alumnos,ComentarioContacto
from .forms import ComentarioContactoForm
import datetime
from django.shortcuts import get_object_or_404
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
def registros(request):

    alumnos=Alumnos.objects.all()
    
#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return consultaContacto(request)
           # comentariosContacto = ComentarioContacto.objects.all() # Fetch all contacts
        #return render(request, 'registros/consultaContacto.html', {'comentariosContacto': comentariosContacto})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def contacto(request):
    
    return render(request,"registros/contacto.html")

    #Indicamos el lugar donde se renderizará el resultado de esta vista
    
def consultaContacto(request):
    comentariosContacto=ComentarioContacto.objects.all()
    return render(request,"registros/consultaContacto.html",{'comentariosContacto':comentariosContacto})

def eliminarComentarioContacto(request, id,
    confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        #comentarios=ComentarioContacto.objects.all()
        #return render(request,"registros/consultaContacto.html",
        #                        {'comentarios':comentarios})
        return consultaContacto(request)
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",
        {'comentarios':comentarios})
        #Si el formulario no es valido nos regresa al formulario para verificar
        #datos
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","image")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio=datetime.date(2024,6,1)
    fechaFin=datetime.date(2025,7,20)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains=" inscrito")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar8(request):
    fechaInicio=datetime.date(2025,7,8)
    fechaFin=datetime.date(2025,7,9)
    comentariosContacto=ComentarioContacto.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultaContacto.html",{'comentariosContacto':comentariosContacto})
def consultar9(request):
    comentariosContacto=ComentarioContacto.objects.filter(mensaje__contains="a")
    return render(request,"registros/consultaContacto.html",{'comentariosContacto':comentariosContacto})
def consultar10(request):
    comentariosContacto=ComentarioContacto.objects.filter(usuario__in=["Maria Antonieta"])
    return render(request,"registros/consultaContacto.html",{'comentariosContacto':comentariosContacto})
def consultar11(request):
    comentariosContacto=ComentarioContacto.objects.all().only("mensaje")
    return render(request,"registros/consultaContacto.html",{'comentariosContacto':comentariosContacto})
def consultar12(request):
    comentariosContacto=ComentarioContacto.objects.filter(mensaje__startswith="Hola")
    return render(request,"registros/consultaContacto.html",{'comentariosContacto':comentariosContacto})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id,matricula,nombre, carrera, turno, image FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def seguridad(request,nombre=None):
    nombre=request.GET.get('nombre')
    return render(request,"registros/seguridad.html",{'nombre':nombre})

