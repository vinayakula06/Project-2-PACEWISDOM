# resume_app/models.py
from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    professional_summary = models.TextField()
    years_experience = models.DecimalField(max_digits=4, decimal_places=1)
    communication_skills = models.TextField()
    web_app_experience = models.TextField()
    os_knowledge = models.CharField(max_length=255)
    code_management_tools = models.CharField(max_length=255)
    google_api_integration = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name
class TechnicalSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='technical_skills')
    category = models.CharField(max_length=255) # e.g., "Programming and Scripting"
    skill_name = models.CharField(max_length=255) # e.g., "JavaScript"
    def __str__(self):
        return f"{self.category}: {self.skill_name}"
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    technologies_used = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.project_name
class EmployeeProject(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role_responsibilities = models.TextField()
    class Meta:
        unique_together = ('employee', 'project')
    def __str__(self):
        return f"{self.employee.name} - {self.project.project_name}"