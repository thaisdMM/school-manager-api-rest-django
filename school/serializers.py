from rest_framework import serializers
from school.models.students import Student
from school.models.courses import Course
from school.models.enrollments import Enrollment
from school.validators import validate_cpf, validate_name, validate_phone_number


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # You can select especific fields
        fields = ["id", "name", "email", "cpf", "date_of_birth", "phone_number"]

    def validate_cpf(self, value: str) -> str:
        """Validate CPF field during serializer input validation before saving,
        using centralized validator."""
        validate_cpf(value)
        return value

    def validate_name(self, value: str) -> str:
        """Validate name field during serializer input validation before saving,
        using centralized validator."""
        validate_name(value)
        return value

    def validate_phone_number(self, value):
        """Validate phone_number field during serializer input validation before saving,
        using centralized validator."""
        validate_phone_number(value)
        return value


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


class ListEnrollmentsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ["course", "period"]

    def get_period(self, obj):
        """
        Return the human-readable value of the 'period' field.

        Uses Django's built-in get_<field>_display() method to convert
        the stored choice value (e.g., 'M') into ist display label (e.g., 'Morning')
        """
        return obj.get_period_display()


class ListEnrollmentsCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source="student.name")

    class Meta:
        model = Enrollment
        fields = ["student_name"]
