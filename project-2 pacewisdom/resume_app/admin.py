# resume_app/admin.py
from django.contrib import admin
from .models import Employee, TechnicalSkill, Project, EmployeeProject
admin.site.register(Employee)
admin.site.register(TechnicalSkill)
admin.site.register(Project)
admin.site.register(EmployeeProject)