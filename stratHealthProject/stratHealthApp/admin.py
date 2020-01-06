from django.contrib import admin
from .models import HospitalGroup, Hospital, Contact, ProcedureCategory, Procedures, Staff


# Register your models here.
admin.site.register(HospitalGroup)
admin.site.register(Hospital)
admin.site.register(Contact)
admin.site.register(ProcedureCategory)
admin.site.register(Procedures)
admin.site.register(Staff)
