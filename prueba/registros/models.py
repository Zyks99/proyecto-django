from django.db import models
# Create your models here.
class Alumnos(models.Model):
    matricula=models.CharField(max_length=12 ,verbose_name="Mat") #el verbose name cambia el nombre del atributo como un alias
    nombre=models.TextField()
    carrera=models.TextField()
    turno=models.CharField(max_length=12)
    image=models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="Alumno"
        verbose_name_plural ="Alumnos"
        ordering = ["-created"]
    def __str__(self):
        return self.nombre     