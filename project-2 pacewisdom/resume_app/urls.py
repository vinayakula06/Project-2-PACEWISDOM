# resume_app/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.resume_search, name='resume_search'),
    path('generate/<int:employee_id>/', views.generate_resume_pdf, name='generate_resume_pdf'),
]