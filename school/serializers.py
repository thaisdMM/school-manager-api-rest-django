from rest_framework import serializers
from school.models.students import Student
from school.models.courses import Course
from school.models.enrollments import Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # You can select especific fields
        fields = ["id", "name", "email", "cpf", "date_of_birth", "phone_number"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # You can select all fields
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        # You can exclude some fields
        # in the example below, none were excluded
        exclude = []
