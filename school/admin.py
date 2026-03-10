from django.contrib import admin

from school.models.courses import Course
from school.models.students import Student


class Students(admin.ModelAdmin):
    list_display = ("id", "name", "email", "cpf", "date_of_birth", "phone_number")
    list_display_links = (
        "id",
        "name",
    )
    list_per_page = 20
    search_fields = ("name",)


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ("id", "code", "description")
    list_display_links = ("id", "code")
    search_fields = ("code",)


admin.site.register(Course, Courses)
