# Create your views here.
from django.apps import apps
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView

from apps.system.forms import NetaChoiceForm
from apps.system.models import Vote

Party = apps.get_model('system', 'Party')

User = get_user_model()


def get_leading_party_queryset():
    parties = Party.objects.all()
    annotated_queryset = parties.annotate(vote_count=Count('vote')).order_by('-vote_count')
    return annotated_queryset


class HomeTemplateView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = dict(
            leading_parties=get_leading_party_queryset(),
            form=NetaChoiceForm
        )
        return context


class SearchResulPage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        import pdb
        pdb.set_trace()
        context = {

        }
        return context


class SuccessHomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = dict(
            leading_parties=get_leading_party_queryset(),
            form=NetaChoiceForm,
            message='Vote Submitted Successfully!!'
        )
        return context


class RegisterTemplateView(TemplateView):
    template_name = 'home/register.html'


class LoginTemplateView(TemplateView):
    template_name = 'home/login.html'


class CreateVoteView(CreateView):
    model = Vote
    fields = ['party', 'constituency']
    success_url = reverse_lazy('home-success')


def home_view(request, show_result=False,*args, **kwargs):
    # report type choices are 'view-mjp', 'view-daily-working', 'view-final-claim'
    context = {}
    print(args, kwargs, show_result)
    if request.method == 'GET':
        context['form'] = NetaChoiceForm
    else:
        form = NetaChoiceForm(data=request.POST)
        if form.is_valid():
            party = form.cleaned_data['party']
            constituency = form.cleaned_data['constituency']
            search_results = User.objects.filter(party=party, constituency=constituency)
            context['is_search_result'] = True
            context['search_results'] = search_results
            context['is_result_empty'] = search_results.count() == 0

        context['form'] = NetaChoiceForm(data=request.POST)
    return TemplateResponse(
        request,
        'home/index.html',
        context=context
    )


@csrf_exempt
def vote_a_member(request, member_pk):
    member = get_object_or_404(User, pk=member_pk)
    Vote.objects.create(vote_for=member)
    if request.method == 'GET':
        return redirect('home')

    context = {}
    context['is_result'] = True
    context['form'] = NetaChoiceForm
    context['leading_parties'] = get_leading_party_queryset()
    context['message'] = 'Your vote has been submitted successfully'
    return TemplateResponse(
        request,
        'home/index.html',
        context=context
    )
