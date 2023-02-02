from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'city'],
                                    name='name_city_constraint')
        ]

    def __str__(self):
        return self.name
