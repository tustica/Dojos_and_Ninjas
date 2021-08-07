from django.http.response import HttpResponse
from django.shortcuts import render
from .models import users

def index(request):
    return render(request, 'index.html')

def process(request):
    new_user = users.objects.create(first_name = request.POST['first_name'], 
    last_name = request.POST['last_name'], email = request.POST['email'], age=request.POST['age'])
    context = {
        "all_users": users.objects.all()
    }
    return render(request, 'index.html', context)