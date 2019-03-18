"""KnowYourNeta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.authuser.views import CreateUserView, Login
from apps.system.views import RegisterTemplateView, LoginTemplateView, CreateVoteView, \
    SuccessHomePage, home_view, vote_a_member, PoliticianDetailViewSet, SearchResultView, VoteAMember, AssemblyListView, \
    ConstituencyListView, PartyListView, LeaderboardListView, DistrictListView, GetUserDetailView, MessageListAPIView, \
    GetUserDetailViewWithID, AllPoliticianListView

router = routers.DefaultRouter()
router.register(r'politician_data', PoliticianDetailViewSet, base_name='politician_detail')
router.register(r'party', PartyListView, base_name='party')
router.register(r'constituency', ConstituencyListView, base_name='constituency')
router.register(r'assembly-segment', AssemblyListView, base_name='assembly_segment')
router.register(r'district', DistrictListView, base_name='district')
urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', home_view, name='home'),
                  path('success/', SuccessHomePage.as_view(), name='home-success'),
                  path('register/', RegisterTemplateView.as_view(), name='register'),
                  path('login/', LoginTemplateView.as_view(), name='login'),
                  path('vote/', CreateVoteView.as_view(), name='vote'),
                  path('vote-member/<int:member_pk>/', vote_a_member, name='vote_member'),
                  url(r'^api-auth/', include('rest_framework.urls')),

                  url(r'^api/', include(router.urls)),

                  url('api/signup/', CreateUserView.as_view(), name='create_user'),
                  path('api/login/', Login.as_view(), name='login'),
                  path('api/search/', SearchResultView.as_view(), name='search'),
                  path('api/vote/', VoteAMember.as_view(), name='vote'),
                  path('api/leaderboard/', LeaderboardListView.as_view(), name='vote'),
                  path('api/all-politician/', AllPoliticianListView.as_view(), name='all_politician'),
                  path('api/message', MessageListAPIView.as_view(), name='message'),
                  path('api/get-user-detail-by-username/<str:username>', GetUserDetailView.as_view(),
                       name='user_detail'),
                  path('api/get-user-detail-by-id/<int:user_id>', GetUserDetailViewWithID.as_view(),
                       name='user_detail_id_wise'),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
