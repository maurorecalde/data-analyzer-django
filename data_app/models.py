from django.db import models

class ArchivoCSV(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='csv/')

    def __str__(self):
        return self.nombre
