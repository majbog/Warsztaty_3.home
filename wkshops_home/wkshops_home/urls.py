"""wkshops_home URL Configuration

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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from contact_book.views import ShowAllContactsView, NewContactView, ContactDetailsView, AllGroupsView, \
    AddPhoneView, AddMailView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^main/$', ShowAllContactsView.as_view(), name="index"),
    url(r'^new/$', NewContactView.as_view(), name='new-contact'),
    url(r'^contact/(?P<contact_id>(\d+))/$', ContactDetailsView.as_view(), name='contact-details'),
    url(r'^contact/(?P<contact_id>(\d+))/add_phone/$', AddPhoneView.as_view(), name='add-phone'),
    url(r'^contact/(?P<contact_id>(\d+))/add_mail/$', AddMailView.as_view(), name='add-mail'),
    url(r'^group/show-all/$', AllGroupsView.as_view(), name='all-groups')
]
