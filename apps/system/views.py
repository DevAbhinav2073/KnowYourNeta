# Create your views here.
from django.views.generic import TemplateView

from apps.system.models import Party


def get_leading_party_queryset():
    parties = Party.objects.all()


class HomeTemplateView(TemplateView):
    template_name = 'home/index.html'


class RegisterTemplateView(TemplateView):
    template_name = 'home/register.html'


class LoginTemplateView(TemplateView):
    template_name = 'home/login.html'
