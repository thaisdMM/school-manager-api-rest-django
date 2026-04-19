# School Manager API - Django REST Framework

This repository contains the development of a school management API using Django REST Framework (DRF), following Alura's educational path.

## Project Structure

The project is divided into branches, where each branch corresponds to a specific course and set of features:

### 1. Main Branch: Building RESTful APIs from Zero
**Course:** "Django REST Framework: Construindo APIs RESTful do Zero"

Focuses on the fundamentals of DRF:
- **API Development:** Building a complete API from scratch with Python and Django.
- **Core Components:** Working with Models, Serializers, Views, ViewSets, and Routers.
- **Django Admin:** Integrating the admin panel and exploring the API Root.
- **Security:** Implementing basic authentication and permissions.

### 2. Validation & Versioning Branch
**Branch:** `validation-pagination-filter-versioning`
**Course:** "Django REST Framework: Validações, Paginação, Filtros e Versionamento"

Focuses on advanced features and best practices:
- **Validations:** Ensuring data integrity with custom Model and Serializer validations.
- **Pagination:** Improving data navigation and organization.
- **Filters & Search:** Implementing efficient search, filtering, and ordering.
- **Versioning:** Practical strategies for API versioning.

## Prerequisites

- Python 3.x
- Django 6.x
- Django REST Framework

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/thaisdMM/school-manager-api-rest-django.git
   cd school-manager-api-rest-django
   ```

2. **Select the desired branch:**
   ```bash
   git checkout main # For basic API
   # OR
   git checkout validation-pagination-filter-versioning # For advanced features
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Course Highlights

- **Data Integrity:** Implementation of custom validations (CPF, name, and phone numbers) using Regex and validator files.
- **Developer Experience:** Use of API Root for easy navigation and Django Admin for management.
- **Scalability:** Application of pagination and filtering to handle large datasets efficiently.
- **Maintenance:** Implementation of API versioning to ensure backward compatibility.

---
Developed during [Alura](https://www.alura.com.br/) courses.
