from rest_framework import serializers
from school.models.students import Student
from school.models.courses import Course
from school.models.enrollments import Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # You can select especific fields
        fields = ["id", "name", "email", "cpf", "date_of_birth", "phone_number"]

    def validate_cpf(self, cpf):
        """
        Validate CPF field during serialize input validation before saving.

        This method runs when data is received from a request.
        It checks if the CPF contains only numbers and
        is exactly 11 characters before the data is saved.
        """
        if not cpf.isdigit():
            raise serializers.ValidationError("CPF must be only digits!")
        if len(cpf) != 11:
            raise serializers.ValidationError("CPF must be 11 digits!")
        return cpf

    def validate_name(self, name):
        if not name.isalpha():
            raise serializers.ValidationError("Name can be only letters.")
        return name

    def validate_phone_number(self, phone_number):
        if len(phone_number) != 13:
            raise serializers.ValidationError("Phone number must be 13 digits.")
        return phone_number


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
