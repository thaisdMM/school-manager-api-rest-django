from __future__ import annotations
from rest_framework import viewsets

from school.models import Student
from school.models import Course
from school.serializers import StudentSerializer, CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
