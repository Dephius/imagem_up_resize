from django.conf.urls import url
from django.contrib import admin

from meuprojeto.appupload.views import galeria

urlpatterns = [
    url(r'^lista/', galeria, name='galeria'),
   ]