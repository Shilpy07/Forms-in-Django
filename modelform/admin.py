from django.contrib import admin

from modelform.models import StudentRecord
from modelform.models import CustomerRecord
from modelform.models import CustomerRecord1


# Register your models here.

class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment', 'faculty', 'year', 'register_date', 'address')
    search_fields = ('name', 'enrollment', 'faculty', 'register_date')


class CustomerRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_id')
    search_fields = ('name', 'customer_id')


admin.site.register(StudentRecord, StudentRecordAdmin)
admin.site.register(CustomerRecord, CustomerRecordAdmin)
admin.site.register(CustomerRecord1)
