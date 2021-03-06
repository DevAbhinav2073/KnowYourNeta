from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.constants import RESERVED_FOR_CHOICES_TUPLE

User = get_user_model()


class State(models.Model):
    name = models.CharField(max_length=70)
    code = models.IntegerField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Constituency(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True)
    link = models.URLField(blank=True, null=True)
    reserved_for = models.CharField(choices=RESERVED_FOR_CHOICES_TUPLE, max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = 'Constituency'
        verbose_name_plural = 'Constituencies'

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/logo/', null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def total_votes(self):
        return self.vote.all().count()

    class Meta:
        verbose_name = 'Party'
        verbose_name_plural = 'Parties'


class AssemblySegment(models.Model):
    name = models.CharField(max_length=100)
    number_of_electorates = models.IntegerField()
    constituency_number = models.CharField(max_length=100)
    reserved_for = models.CharField(choices=RESERVED_FOR_CHOICES_TUPLE, max_length=40, null=True, blank=True)
    constituency = models.ForeignKey(Constituency, on_delete=models.PROTECT)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    vote_for = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.PROTECT, related_name='vote', blank=True, null=True)
    constituency_segment = models.ForeignKey(AssemblySegment, on_delete=models.PROTECT, blank=True,
                                             null=True)
    constituency = models.ForeignKey(Constituency, null=True, blank=True, related_name='votes',
                                     on_delete=models.PROTECT)

    def __str__(self):
        return 'vote for : %s' % (self.vote_for,)


class Post(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Message(models.Model):
    message_text = models.TextField()
    message_type = models.CharField(max_length=50)

    def __str__(self):
        return self.message_text
