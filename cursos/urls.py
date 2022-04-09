from django.urls import path

from cursos.views import home

urlpatterns = [
    path('', home),
]
