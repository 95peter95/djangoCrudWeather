from django.db import models

class Job(models.Model):
    name=models.CharField(max_length=100)

class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    job=models.ForeignKey(Job, on_delete=models.CASCADE , default=None, blank=True, null=True)
    age=models.IntegerField()

class City(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


