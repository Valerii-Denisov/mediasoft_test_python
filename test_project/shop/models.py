from django.db import models
from test_project.city.models import Street
from django.core.validators import MinValueValidator


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200, unique=True)
    city = models.ForeignKey(Street, on_delete=models.CASCADE, to_field='city')
    # street = models.ForeignKey()
    house = models.SmallIntegerField(validators=[MinValueValidator(0)])
    timestamp = models.DateTimeField(auto_now_add=True)
    is_open = models.TimeField()
    is_close = models.TimeField()


    def __str__(self):
        return self.name
