from django.db import models
from test_project.city.models import Street, City
from django.core.validators import MinValueValidator
import time


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, null=True)
    house = models.SmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1,
    )
    to_open_time = models.TimeField(null=True)
    to_close_time = models.TimeField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_true_city(self):
        street_city = Street.object.get(id=self.street)['city']
        return self.city['name'] == street_city

    @property
    def is_open(self):
        t = time.localtime()
        t = time.strftime('%H:%M:%S', t)
        if str(self.to_open_time) < t < str(self.to_close_time):
            return 1
        else:
            return 0
