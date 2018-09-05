from .models import  TempKeys
from .serializers import KeySerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class keyList(APIView):
    def get(self,request, format=None):
        keys = TempKeys.objects.all()
        serialized_keys = KeySerializer(keys, many=True)
        return Response(self.serialized_keys.data)

class KeyDetail(APIView):

    def get_object(self, pk):
        try:
            return TempKeys.object.get(pk=pk)
        except TempKeys.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):
        key = self.get_object(pk)
        serialized_key = KeySerializer(key)
        return Response(serialized_key.date)



