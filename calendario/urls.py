from django.urls import path
from .views import *

urlpatterns = [
    path("", CalendarioView.as_view()),

    # EVENTOS
    path("eventos/", EventoListView.as_view()),
    path("eventos/create/", EventoCreateView.as_view()),
    path("eventos/update/<int:id>/", EventoUpdateView.as_view()),
    path("eventos/delete/<int:id>/", EventoDeleteView.as_view()),

    # TAGS
    path("tags/", TagListView.as_view()),
    path("tags/create/", TagCreateView.as_view()),
    path("tags/delete/<int:id>/", TagDeleteView.as_view()),
]