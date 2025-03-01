from .models import CourseDetail,CourseDescription
from rest_framework import serializers


class CourseDescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseDescription
        fields = ('__all__')
        
    def get_image_url(self, obj):
        request = self.context.get('request')  # Get the current request context
        if obj.image:
            return request.build_absolute_uri(obj.image.url)  # Generate the absolute URL
        return None

class CourseDetailSerializers(serializers.ModelSerializer):
    CourseDesc = CourseDescriptionSerializers(many=True , read_only= True)
    class Meta:
        model = CourseDetail
        fields = ['id','CourseName','CourseDesc']
