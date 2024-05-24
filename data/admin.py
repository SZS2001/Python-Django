from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','Student_Name','Student_DOB','Student_DOJ')

