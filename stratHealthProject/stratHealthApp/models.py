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
    hospital_hospitalgroup = models.ForeignKey(HospitalGroup, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.hospital_name


class Contact(models.Model):
    contact_django_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    contact_name = models.CharField(max_length=200)
    contact_address = models.CharField(max_length=200, blank=True)
    contact_phone = models.CharField(max_length=200, blank=True)
    contact_position = models.CharField(max_length=200, blank=True)
    contact_hospital_list = models.ManyToManyField(Hospital, blank=True)

    def __str__(self):
        return self.contact_name


class ProcedureCategory(models.Model):
    procedure_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.procedure_category_name


class Staff(models.Model):
    staff_name = models.CharField(max_length=200)
    staff_startDate = models.DateField()
    staff_position = models.CharField(max_length=200, blank=True)
    staff_salary = models.DecimalField(max_digits=13, decimal_places=3, blank=True)
    staff_hospital_list = models.ManyToManyField(Hospital, blank=True)

    def __str__(self):
        return self.staff_name


class Procedures(models.Model):
    procedure_staff_list = models.ManyToManyField(Staff, blank=True)
    procedure_name = models.CharField(max_length=300)
    procedure_description = models.CharField(max_length=1000, blank=True)
    procedure_date = models.DateTimeField()
    procedure_cost = models.DecimalField(max_digits=16, decimal_places=3, blank=True)
    procedure_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    procedure_category = models.ForeignKey(ProcedureCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.procedure_name
