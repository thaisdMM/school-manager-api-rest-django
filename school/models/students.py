from __future__ import annotations

from django.db import models

from school.validators import validate_cpf, validate_name, validate_phone_number


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, validators=[validate_name])
    email = models.EmailField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf])
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])

    def __str__(self) -> str:
        return f"Student: {self.name}"
