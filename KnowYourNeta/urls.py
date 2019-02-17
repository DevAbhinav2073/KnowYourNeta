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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.system.views import HomeTemplateView, RegisterTemplateView, LoginTemplateView, CreateVoteView, \
    SuccessHomePage, home_view, vote_a_member

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', home_view, name='home'),
                  path('success/', SuccessHomePage.as_view(), name='home-success'),
                  path('register/', RegisterTemplateView.as_view(), name='register'),
                  path('login/', LoginTemplateView.as_view(), name='login'),
                  path('vote/', CreateVoteView.as_view(), name='vote'),
                  path('vote-member/<int:member_pk>/', vote_a_member, name='vote_member'),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
