from django.shortcuts import render
from django.http import HttpResponse
from .models import about

# Create your views here.

def index(request):
    return render(request, 'index.html')

def insert_about(request):
    return render(request, 'insert_about.html')

def get_about(request):
    if request.method == 'POST':
        about_obj = about()

        fname = request.POST.get('fullname')
        about_obj.name = fname

        email = request.POST.get('email')
        about_obj.email = email

        phone = request.POST.get('phone')
        about_obj.phone = phone

        birth_date = request.POST.get('dob')
        about_obj.birth_date = birth_date

        nationality = request.POST.get('nationality')
        about_obj.nationality = nationality
        

        # saving the form
        about_obj.save()

        return HttpResponse(about_obj)
    return HttpResponse('not found')

