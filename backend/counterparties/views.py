from rest_framework import generics
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.serializers import serialize

from counterparties.models import Counterparties
from counterparties.serializers import CounterpartiesSerializer


from rest_framework.response import Response

class CounterpartiesView(APIView):
    def get(self, request):
        counterparties = Counterparties.objects.all()
        serializer = CounterpartiesSerializer(counterparties, many=True)
        return Response({"counterparties": serializer.data})