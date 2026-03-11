from rest_framework import serializers
from school.models.students import Student
from school.models.courses import Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "email", "cpf", "date_of_birth", "phone_number"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
