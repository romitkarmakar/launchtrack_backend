from django.db import models

class Spaceport(models.Model):
    name = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200, default='')
    image = models.CharField(max_length=200, default='')
    details = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name

class Launch(models.Model):
    name = models.CharField(max_length=200, default='')
    date = models.DateTimeField(blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    image = models.CharField(max_length=200, default=' ')
    location = models.CharField(max_length=200, default='')
    details = models.TextField(max_length=1000, default='')
    payload = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name