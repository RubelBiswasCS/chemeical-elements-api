from base.models import Elements
from .serializers import ElementsSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ElementsList(generics.ListCreateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields = ['group','period',]
    ordering_fields = ['group','atomic_number','atomic_weight',]
    search_fields = ['=name','=symbol',]

class ElementsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer


