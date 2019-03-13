# Create your views here.
from django.apps import apps
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.authuser.serializers import UserSerializer
from apps.constants import USER_TYPE_POLITICIAN
from apps.system.forms import NetaChoiceForm
from apps.system.serializers import *

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


def home_view(request, show_result=False, *args, **kwargs):
    # report type choices are 'view-mjp', 'view-daily-working', 'view-final-claim'
    context = {}
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


class PoliticianDetailViewSet(ModelViewSet):
    serializer_class = PoliticianDetailSerializer
    queryset = PoliticianDetail.objects.all()

    def create(self, request, *args, **kwargs):
        user_pk = request.user.pk
        self.request.data['detail_of'] = request.user.pk
        if PoliticianDetail.objects.filter(id=user_pk).exists():
            politician_detail = PoliticianDetail.objects.filter(id=user_pk)
            politician_detail.update(**self.request.data)
            politician_detail = politician_detail.get(pk=user_pk)
        else:
            serialized = PoliticianDetailSerializer(data=request.data)
            if serialized.is_valid(raise_exception=True):
                politician_detail = serialized.save()
        return Response(PoliticianDetailSerializer(politician_detail).data)


class SearchResultView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(user_type=USER_TYPE_POLITICIAN)

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if self.request.GET['party']:
            queryset = queryset.filter(party=self.request.GET['party'])
        if self.request.GET['constituency']:
            queryset = queryset.filter(constituency=self.request.GET['constituency'])
        return queryset


class VoteAMember(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
    permission_classes = [AllowAny, ]


class PartyListView(ModelViewSet):
    serializer_class = PartySerializer
    queryset = Party.objects.all()
    permission_classes = [AllowAny, ]


class DistrictListView(ModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()
    permission_classes = [AllowAny, ]


class ConstituencyListView(ModelViewSet):
    serializer_class = ConstituencySerializer
    queryset = Constituency.objects.all()


class AssemblyListView(ModelViewSet):
    serializer_class = AssemblySegmentSerializer
    queryset = AssemblySegment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('constituency', None):
            queryset = queryset.filter(constituency=self.request.GET['constituency'])
        if self.request.GET.get('constituency_number', None):
            queryset = queryset.filter(constituency_number=self.request.GET['constituency_number'])
        return queryset


class LeaderboardListView(ListAPIView):
    serializer_class = PartySerializer
    queryset = Party.objects.all()

    def get_queryset(self):
        return get_leading_party_queryset()
