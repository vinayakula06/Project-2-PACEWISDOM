# resume_app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa
import os
from .models import Employee, TechnicalSkill, Project, EmployeeProject
def link_callback(uri, rel):
    if uri.find(settings.MEDIA_URL) != -1:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.find(settings.STATIC_URL) != -1:
        path = finders.find(uri.replace(settings.STATIC_URL, ""))
        if not path:
            path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
        # Convert to string if it's a list (from finders.find)
        elif isinstance(path, list):
            path = path[0] if path else ""
    else:
        return uri
    if path and not os.path.isfile(path):
        raise Exception(f'Media URI must start with {settings.STATIC_URL} or {settings.MEDIA_URL}')
    return path

def resume_search(request):
    employees = Employee.objects.all().order_by('name')
    context = {
        'employees': employees
    }
    return render(request, 'resume_app/search_resume.html', context)
def generate_resume_pdf(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    technical_skills = TechnicalSkill.objects.filter(employee=employee).order_by('category', 'skill_name')
    employee_projects = EmployeeProject.objects.filter(employee=employee).select_related('project').order_by('project__project_name')
    context = {
        'employee': employee,
        'technical_skills': technical_skills,
        'employee_projects': employee_projects,
    }
    template = get_template('resume_app/resume_template.html')
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{employee.name.replace(" ", "_")}.pdf"'
    try:
        result = pisa.CreatePDF(
            html,                    # the HTML to convert
            dest=response,           # file handle to receive result
            encoding='UTF-8',        # ensure proper encoding
            link_callback=link_callback  # handle static files properly
        )
    except Exception as e:
        return HttpResponse(f'Error generating PDF: {str(e)}<pre>' + html + '</pre>')
    return response