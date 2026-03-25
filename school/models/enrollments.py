from __future__ import annotations

from django.db import models

from .students import Student
from .courses import Course


class Enrollment(models.Model):
    """
    Enrollment model to connect Student and Course.
    It has many to one relationship.
    """

    PERIOD = (("M", "Morning"), ("A", "Afternoon"), ("N", "Night"))
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, choices=PERIOD, blank=False, null=False, default="M"
    )

    def __str__(self):
        return f"{self.student} | {self.course}"
