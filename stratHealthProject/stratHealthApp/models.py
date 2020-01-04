from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class HospitalGroup(models.Model):
    hospital_group_name = models.CharField(max_length=200)

    def __str__(self):
        return self.hospital_group_name


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=200)
    hospital_address = models.CharField(max_length=200)
    hospital_hospitalGroup = models.ForeignKey(HospitalGroup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.hospital_name


class Contact(models.Model):
    contact_djangoUser = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    contact_name = models.CharField(max_length=200)
    contact_address = models.CharField(max_length=200, blank=True)
    contact_phone = models.CharField(max_length=200, blank=True)
    contact_jobTitle = models.CharField(max_length=200, blank=True)
    contact_hospitalGroup = models.ManyToManyField(Hospital, blank=True)

    def __str__(self):
        return self.contact_name
