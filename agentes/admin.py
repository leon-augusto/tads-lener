from django.contrib import admin
from .models import Student, Teacher


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['photo_preview', 'name', 'course', 'group']
    list_filter = ['course']
    """
    Admin class for managing Student records.
    """


class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['photo_preview', 'name', 'email']
    list_filter = ['groups']
    """
    Admin class for managing Teacher records.
    """


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
