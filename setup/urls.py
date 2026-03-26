from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from school.views import (
    StudentViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    ListEnrollmentsStudentView,
    ListEnrollmentsCourseView,
)

router = routers.DefaultRouter()
router.register(prefix="students", viewset=StudentViewSet, basename="Students")
router.register(prefix="courses", viewset=CourseViewSet, basename="Courses")
router.register(prefix="enrollments", viewset=EnrollmentViewSet, basename="Enrollment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("students/<int:pk>/enrollments", ListEnrollmentsStudentView.as_view()),
    path("courses/<int:pk>/enrollments", ListEnrollmentsCourseView.as_view()),
]
