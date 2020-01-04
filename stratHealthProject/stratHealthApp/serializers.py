from django.contrib.auth.models import User, Group
from .models import HospitalGroup, Hospital, Contact
from rest_framework import serializers


class HospitalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalGroup
        fields = "__all__"


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
