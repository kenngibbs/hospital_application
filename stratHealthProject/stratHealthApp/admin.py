from django.contrib import admin
from .models import HospitalGroup, Hospital, Contact


# Register your models here.
admin.site.register(HospitalGroup)
admin.site.register(Hospital)
admin.site.register(Contact)
