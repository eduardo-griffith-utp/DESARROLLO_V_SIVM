from rest_framework import serializers
from .models import Example
class ExampleSerializer(serializers.ModelSerializer):
   class Meta:
        model = Example
        fields = ['id', 'name', 'description', 'created_at', 'resumen']

   def get_resumen(self, obj):
        if obj.description:
            return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
        return "Sin descripción"