# Create your views here.
from django.apps import apps
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from apps.system.forms import VoteForm
from apps.system.models import Vote

Party = apps.get_model('system', 'Party')


def get_leading_party_queryset():
    parties = Party.objects.all()
    annotated_queryset = parties.annotate(vote_count=Count('vote')).order_by('-vote_count')
    return annotated_queryset


class HomeTemplateView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = dict(
            leading_parties=get_leading_party_queryset(),
            form=VoteForm
        )
        return context

class SuccessHomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = dict(
            leading_parties=get_leading_party_queryset(),
            form=VoteForm,
            message = 'Vote Submitted Successfully!!'
        )
        return context

class RegisterTemplateView(TemplateView):
    template_name = 'home/register.html'


class LoginTemplateView(TemplateView):
    template_name = 'home/login.html'


class CreateVoteView(CreateView):
    model = Vote
    fields = [
        'party', 'assembly_constituency_name',
    ]
    success_url = reverse_lazy('home-success')
