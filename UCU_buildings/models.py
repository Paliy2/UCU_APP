from django.db import models


class Building(models.Model):
    '''
    Street Location
    Name
    Description
    '''
    location = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    description = models.TextField()
