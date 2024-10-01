from django.db import models


# Create your models here.


class TODO1(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    datefield = models.DateField()


def __self(self):
    return self.name
