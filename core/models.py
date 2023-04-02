from django.db import models

# Create your models here.
class contactos(models.Model):
    contactos = models.CharField(max_length=250)

    def __str__(self):
        return self.contactos
