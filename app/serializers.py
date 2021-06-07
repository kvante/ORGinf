from rest_framework import serializers
from .models import Organization, TopManager


class TopManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopManager
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    topmanager = TopManagerSerializer(many=True)

    class Meta:
        model = Organization
        fields = '__all__'
