from django.db import models
from django.contrib.auth.models import User

class Event(models.group):
  tema=models.CharField(max_length=250)
  encargado=models.ForeignKey(User,on_delete=models.CASCADE,related_name="encargado")
  descripcion=models.TextField(blank=True,null=True)
  ubicacion=models.CharField(max_length=200)
  fecha_y_hora=models.DateTimeField(auto_now=True)
  asistentes=models.ManyToManyField(User,related_name="asistentes",through='asistentes')
  def __str__(self):
    return self.tema
