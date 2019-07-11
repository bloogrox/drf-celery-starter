from django.db import models


class Sample(models.Model):
    name = models.CharField(max_length=64)
