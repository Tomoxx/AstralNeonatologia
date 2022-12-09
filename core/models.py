from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sector(models.Model):
    tipos = [('UTI','UTI'),('UCI','UCI')]
    tipo = models.CharField(max_length=3, choices=tipos)
    def __str__(self) -> str:
        return 'Sector Numero '+ str(self.id) + ' (' + self.tipo + ")"
    
class Cama(models.Model):
    sector = models.ForeignKey('Sector', on_delete=models.SET_NULL, null=True)
    
class RecienNacido(models.Model):
    nombre = models.CharField(max_length=50)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50,blank=True,default='')
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.nombre + self.paterno + self.materno
    
# class Padres(models.Model):
#     padres = User.objects.filter(groups__name='Padres')

class Evolucion(models.Model):
    fecha = models.DateField()
    peso = models.IntegerField()
    orina = models.BooleanField()
    deposicion = models.BooleanField()
    tolerancia = models.CharField(max_length=50)
    cama = models.ForeignKey('Cama', on_delete=models.DO_NOTHING)
    recienNacido = models.ForeignKey('RecienNacido', on_delete=models.CASCADE)
    matrona = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Matronas", limit_choices_to={'groups__name':"Matronas"}, null=True)
    # padres = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Matronas", limit_choices_to={'groups__name':"Matronas"}, null=True)
