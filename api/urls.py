from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('elements/', views.ElementsList.as_view(),name='elements'),
    path('elements/<int:pk>/', views.ElementsDetails.as_view(),name='elementsdetails'),
]
