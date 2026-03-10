from __future__ import annotations

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=14)

    def __str__(self) -> str:
        return f"Student: {self.name}"
