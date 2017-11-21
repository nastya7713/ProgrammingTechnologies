from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  *
from .forms import *
# Register your models here.

class RegisterListAdmin(admin.ModelAdmin):
    form = RegisterListForm

class FacultyEnrolleeAdmin(admin.ModelAdmin):
    list_display = ['faculty','enrollee', 'average_grade', 'check_status']

class EnrolleeAdmin(admin.ModelAdmin):
    list_display=['user','first_name', 'last_name', 'email']
    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name
    def email(self, obj):
        return obj.user.email

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty_limit']

class FacultySubjectAdmin(admin.ModelAdmin):
    list_display = ['faculty_name', 'subjects']
    def faculty_name(self, obj):
        return obj.faculty.name
    def subjects(self, obj):
        return ','.join([a.name for a in obj.subject.all()])

admin.site.register(FacultyEnrollee, FacultyEnrolleeAdmin)
admin.site.register(RegisterList, RegisterListAdmin)
admin.site.register(Enrollee, EnrolleeAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(FacultySubject, FacultySubjectAdmin)
admin.site.register(Subject)
