from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    mensaje = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return {"mensaje": validated_data['mensaje']}