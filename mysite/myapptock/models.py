from django.db import models


class Cust(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)