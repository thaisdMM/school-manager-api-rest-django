from __future__ import annotations
from rest_framework import viewsets, generics


from school.models import Student
from school.models import Course
from school.models import Enrollment
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    ListEnrollmentsCourseSerializer,
    ListEnrollmentsStudentSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class ListEnrollmentsStudentView(generics.ListAPIView):

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListEnrollmentsStudentSerializer


class ListEnrollmentsCourseView(generics.ListAPIView):

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListEnrollmentsCourseSerializer
