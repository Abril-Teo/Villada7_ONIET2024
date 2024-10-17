from django.db import models

# Create your models here.
class Registro(models.Model):
    registro = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=100)
    mes = models.PositiveSmallIntegerField()
    produccionTotal = models.IntegerField()
    cantidaPiezasConFallas = models.IntegerField()
    