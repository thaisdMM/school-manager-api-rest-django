from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from school.views import StudentViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register(prefix="students", viewset=StudentViewSet, basename="Students")
router.register(prefix="courses", viewset=CourseViewSet, basename="Courses")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
