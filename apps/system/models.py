from django.db import models

# Create your models here.
from apps.constants import RESERVED_FOR_CHOICES_TUPLE


class CandidateDetail(models.Model):
    pass


class State(models.Model):
    name = models.CharField(max_length=70)
    code = models.IntegerField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/logo/', null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class AssemblyConstituencyName(models.Model):
    name = models.CharField(max_length=100)
    assembly_segments = models.CharField(max_length=100)
    constituency_number = models.CharField(max_length=100)
    reserved_for = models.CharField(choices=RESERVED_FOR_CHOICES_TUPLE, max_length=40, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
