from django.contrib import admin
from .models import Alumnos,Comentario,ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('matricula','nombre','carrera','turno','created')  
    search_fields=('matricula','nombre','carrera','turno')
    date_hierarchy='created'
    list_filter=('carrera','turno')  
    list_per_page=5 #paginacion
    list_display_links=('matricula','nombre') #que atributos pueden usarse para editar
    list_editables=('turno') #permite editar el atributo desde la lista
    def get_readonly_fields(self, request, obj = ...):
        #si el usuario pertenece al grupo USUARIO
        if request.user.groups.filter(name="Usuarios").exists():
            #bloquea los campos
            return ('created','updated','matricula','carrera','turno')
        else:
            return ('created','updated')
admin.site.register(Alumnos,AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display=('id','coment')
    search_fields=('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')
    def get_readonly_fields(self, request, obj = ...):
        #si el usuario pertenece al grupo GrupoA
        if request.user.groups.filter(name="GrupoA").exists():
            #bloquea los campos
            return ('alumno','id','created')
        else:
            return ('id','created')
admin.site.register(Comentario,AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id','usuario', 'mensaje','created')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
