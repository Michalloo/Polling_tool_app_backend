from rest_framework import serializers
from PollingToolApp.models import Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('answer',)