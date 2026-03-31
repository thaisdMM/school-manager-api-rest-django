from __future__ import annotations

import re

from django.core.exceptions import ValidationError


def validate_cpf(cpf: str) -> None:
    """Validate that CPF contains exactly 11 numeric digits."""
    stripped_cpf = cpf.strip()
    if not stripped_cpf:
        raise ValidationError("CPF cannot be empty.")
    if not stripped_cpf.isdigit():
        raise ValidationError("CPF must contain only numeric digits.")
    if len(stripped_cpf) != 11:
        raise ValidationError("CPF must be exactly 11 digits long.")


def validate_name(name: str) -> None:
    """Validate that name contains only letters, spaces, and hyphens."""
    stripped_name = name.strip()
    if not stripped_name:
        raise ValidationError("Name cannot be blank.")
    if not re.fullmatch(r"^[^\W\d_]([^\W\d_\s]|[\s\-])*$", stripped_name, re.UNICODE):
        raise ValidationError("Name must contain only letters, spaces, or hyphens.")


def validate_phone_number(phone_number: str) -> None:
    """Validate that phone number contains exactly 13 numeric digits."""
    stripped_phone_number = phone_number.strip()
    if not stripped_phone_number:
        raise ValidationError("Phone number cannot be empty.")
    if not stripped_phone_number.isdigit():
        raise ValidationError("Phone number must contain only numeric digits.")
    if len(stripped_phone_number) != 13:
        raise ValidationError("Phone number must be exactly 13 digits long.")
