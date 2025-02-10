from django.db import models

# Create your models here.
class CourseDetail(models.Model):
    CourseName = models.TextField()

    def __str__(self):
        return self.CourseName
    
class CourseDescription(models.Model):
    title = models.ForeignKey(CourseDetail, on_delete=models.CASCADE, related_name='CourseDesc')
    syllabus = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='CourseImage/',default='null')

    # def __str__(self):
    #     return self.title