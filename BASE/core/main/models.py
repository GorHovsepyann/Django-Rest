from django.db import models

# Create your models here.

class Car(models.Model):
    
    name = models.CharField('Car name',max_length=250,help_text = 'Enter car name')
    price = models.PositiveIntegerField('Car price',help_text = 'Enter car price')
    img = models.ImageField('Car image',help_text = 'Enter car image')
    
    def __str__(self) -> str:
        return self.name