# Technical Debt: CPF Validation Strategy

## Context

Currently, CPF validation is implemented only at the serializer level using Django REST Framework. The validation ensures that the CPF:

- Contains exactly 11 characters
- Contains only numeric digits

This approach works for API input validation but does not guarantee data integrity at the model/database level.

---

## Identified Issues

1. **Validation limited to serializers**
   - Data inserted outside the API layer (e.g., Django shell, admin, scripts) may bypass validation.

2. **Duplication risk**
   - If validation is later added to models, logic may be duplicated across multiple layers.

3. **Lack of centralized validation logic**
   - CPF validation rules are not reusable across the application.

---

## Proposed Improvements (Deferred)

The following improvements are intentionally postponed to align with course progression and avoid conflicts with upcoming implementations:

### 1. Centralize CPF validation logic

- Create a reusable validation function in a dedicated module (e.g., `utils/validators.py`).

### 2. Add validation at the model level

- Use Django model field `validators` to enforce constraints at the database level.
- Ensure that invalid CPF values cannot be persisted regardless of the data entry point.

### 3. Reuse validation in serializers

- Integrate the centralized validation logic into serializers to maintain consistent behavior.
- Adapt error handling to use DRF-specific `ValidationError`.

### 4. (Optional - Future Enhancement)

- Implement full CPF validation including check digit verification.

---

## Rationale for Deferring

- The current implementation follows the structure introduced in the course.
- Premature refactoring may conflict with upcoming lessons.
- The goal is to revisit and improve the architecture after completing the course module.

---

## Status

- [ ] Validation centralized
- [ ] Model-level validation implemented
- [ ] Serializer integration aligned with centralized logic
- [ ] CPF algorithm validation implemented

---

## Notes

This technical debt is acknowledged and intentional.
It should be addressed once the full validation strategy taught in the course is understood.
