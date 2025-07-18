
from django.contrib import admin
from django.urls import path, include 
from django.shortcuts import redirect
def redirect_to_resume(request):
    return redirect('resume/')
urlpatterns = [
    path('', redirect_to_resume, name='home'),
    path('admin/', admin.site.urls),
    path('resume/', include('resume_app.urls')), 
]