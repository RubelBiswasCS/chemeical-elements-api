from base.models import Elements
from .serializers import ElementsSerializer
from rest_framework import generics

class ElementsList(generics.ListCreateAPIView):
    queryset = Elements.objects.all()
    serializer_class = ElementsSerializer


