from django.db import models
class Client(models.Model):
    name = models.CharField(max_length=40)
    sign = models.CharField()
    def __str__(self):
        return f'Имя- {self.name}, знак- {self.sign}'
# Create your models here.
