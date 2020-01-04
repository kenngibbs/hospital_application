# from django.contrib.auth.models import User, Group
from .models import HospitalGroup, Hospital, Contact
from rest_framework import viewsets
from .serializers import HospitalGroupSerializer, HospitalSerializer, ContactSerializer


class HospitalGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HospitalGroup.objects.all()
    serializer_class = HospitalGroupSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
