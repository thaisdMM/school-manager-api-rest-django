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


# (.venv) ➜  escola git:(main) ✗ python manage.py shell
# 14 objects imported automatically (use -v 2 for details).

# Cmd click to launch VS Code Native REPL
# Python 3.14.3 (main, Feb  3 2026, 15:32:20) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from school.models.students import Student
# >>> from school.serializers import StudentSerializer
# >>> queryset = Student.objects.all()
# >>> queryset
# <QuerySet [<Student: Student: Mia Mendes>, <Student: Student: Lucas Gonçalves>]>
# >>> serializer = StudentSerializer(queryset, many= True)
# >>> serializer.data
# [{'id': 1, 'name': 'Mia Mendes', 'email': 'mia@email.com', 'cpf': '12312312311', 'date_of_birth': '2025-12-01', 'phone_number': '319999999999'}, {'id': 2, 'name': 'Lucas Gonçalves', 'email': 'lucas@email.com', 'cpf': '22222222211', 'date_of_birth': '2000-03-02', 'phone_number': '317777777'}]
