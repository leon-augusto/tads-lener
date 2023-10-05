from django.contrib import admin
from .models import Theme, Course, Group


class ThemeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description']


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description', 'get_themes']


class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'data_of_register']


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)
