from django.shortcuts import render
from .serializers import CourseDetailSerializers,CourseDescriptionSerializers
from rest_framework import viewsets
from .models import CourseDetail,CourseDescription

# Create your views here.
# @api_view(['GET'])
class CourseDetailViewSet(viewsets.ModelViewSet):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializers

class CourseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = CourseDescription.objects.all()
    serializer_class = CourseDescriptionSerializers
