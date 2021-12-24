from django.urls import path
from . import views

urlpatterns = [
    path('elements/', views.ElementsList.as_view()),
]
