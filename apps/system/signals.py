from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.system.models import Vote


@receiver(pre_save, sender=Vote)
def manage_vote(sender, instance, *args, **kwargs):
    if instance.vote_for is not None:
        instance.party = instance.vote_for.party
        instance.constituency = instance.vote_for.constituency