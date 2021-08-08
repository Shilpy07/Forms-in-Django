from django.contrib import admin

from modelform.models import StudentRecord


# Register your models here.

class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment', 'faculty', 'year', )
    search_fields = ('name', 'enrollment', 'faculty', 'year', )


admin.site.register(StudentRecord, StudentRecordAdmin)