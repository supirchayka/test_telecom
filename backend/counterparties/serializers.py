from rest_framework import serializers

from counterparties.models import Counterparties, Manager, Cities, Channel, TypeOfService

class CounterpartiesSerializer(serializers.Serializer):
    name = serializers.CharField()
    type_of_counterparties = serializers.CharField()
    vip = serializers.BooleanField()
    city = serializers.CharField()
    typeOfService = serializers.CharField()
    address_from = serializers.CharField()
    address_to = serializers.CharField()
    channel = serializers.CharField()
    ticketDate = serializers.CharField()
    knowsFrom = serializers.CharField()
    manager = serializers.CharField()