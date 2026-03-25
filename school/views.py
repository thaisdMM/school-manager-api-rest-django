from __future__ import annotations
from rest_framework import viewsets

from school.models import Student
from school.models import Course
from school.models import Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
