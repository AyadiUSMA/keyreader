from .models import TempKeys

from rest_framework import serializers


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = TempKeys
        fields = (
            'keytag'
        )