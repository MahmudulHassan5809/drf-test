from rest_framework import serializers


class DecodeSerializer(serializers.Serializer):
    request_id = serializers.CharField()
    account_name = serializers.CharField()
    amount = serializers.CharField()
