from django.db import models


# Create your models here.

class CandidateDetail(models.Model):
    pass


class Party(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AssemblyConstituencyName(models.Model):
    names = models.CharField(max_length=100)

    def __str__(self):
        return self.names
