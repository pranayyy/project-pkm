"""
baseproject URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from pkm_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =  [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.home, name='home'),
    path('buildknowledge',views.Build_Kb.as_view(),name='buildkb'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('setupuser/',views.Set_user.as_view(),name="set_user"),
  #  path('update/', views.Set_user_update.as_view(),name='set_user_update'),
    path('search_form/',views.search_form,name="search_form"),
    path('search/', views.search,name="search"),
    path('terms and conditions/',views.terms,name="terms and conditions"),
    path('basetest/',views.basetest),
    path('sharedknowledge',views.sharedknowledge,name="sharedknowledge"),
    path('help/',views.help,name='help'),
    url('^update_setupuser/(?P<pk>[\w-]+)$', views.Set_user_update.as_view(), name='update'),
    url('^detailknowledge/(\d+)/$',views.detailknolwledge),

            ]

if settings.DEBUG is True:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)