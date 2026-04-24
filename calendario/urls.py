from django.urls import path
from .views import *

urlpatterns = [
    path("", CalendarioView.as_view(), name="calendario"),
    path("eventos/", EventoListView.as_view()),
    path("eventos/create/", EventoCreateView.as_view()),
]