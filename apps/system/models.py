from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.constants import RESERVED_FOR_CHOICES_TUPLE

User = get_user_model()


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
    code = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
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
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    vote_for = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.PROTECT, related_name='vote', blank=True, null=True)
    assembly_constituency_name = models.ForeignKey(AssemblyConstituencyName, on_delete=models.PROTECT, blank=True,
                                                   null=True)

    def __str__(self):
        return 'vote for : %s' % (self.vote_for,)
