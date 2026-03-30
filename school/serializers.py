from rest_framework import serializers
from school.models.students import Student
from school.models.courses import Course
from school.models.enrollments import Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # You can select especific fields
        fields = ["id", "name", "email", "cpf", "date_of_birth", "phone_number"]

    def validate(self, data):
        """
        Validate data field during serializer input validation before saving.
        """
        if not data["cpf"].isdigit():
            raise serializers.ValidationError({"cpf": "CPF must be only digits!"})
        if len(data["cpf"]) != 11:
            raise serializers.ValidationError({"cpf": "CPF must be 11 digits!"})
        if not data["name"].isalpha():
            raise serializers.ValidationError(
                {"name": "Name cannot be alpha - name must be only letters."}
            )
        if len(data["phone_number"]) != 13:
            raise serializers.ValidationError(
                {"phone_number": "Phone number must be 13 digits."}
            )
        return data


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
