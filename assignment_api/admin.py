from django.contrib import admin
from .models import CourseDetail,CourseDescription
# Register your models here.

# @admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ['CourseName']


# @admin.register(CourseDescription)
class CourseDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title','syllabus','description']

admin.site.register(CourseDetail,CourseDetailAdmin)    
admin.site.register(CourseDescription,CourseDescriptionAdmin)    
