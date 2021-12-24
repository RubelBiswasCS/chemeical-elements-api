from rest_framework import serializers
from base.models import Elements

class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = ['name', 'atomic_number', 'atomic_weight', 'symbol',	'melting_point', 'boiling_point', 'group', 'period', 'electron_configuration']
