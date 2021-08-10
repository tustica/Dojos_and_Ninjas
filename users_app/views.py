from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import dojos, ninjas, users

def index(request):
    return render(request, 'index.html')

def dojos_and_ninjas(request):
    context = {
        "all_dojos": dojos.objects.all(),
        "all_ninjas": ninjas.objects.all()
    }
    return render(request, 'dojos_and_ninjas.html', context)

def process_dojo(request):
    dojos.objects.create(dojo_name = request.POST['dojo_name'],
    dojo_city = request.POST['dojo_city'], dojo_state = request.POST['dojo_state'])
    return redirect('/dojos')

def process_ninja(request):
    ninjas.objects.create(first_name = request.POST['first_name'],
    last_name = request.POST['last_name'], dojo = dojos.objects.get(id=request.POST['dojo_select']))
    return redirect('/dojos')

def process(request):
    new_user = users.objects.create(first_name = request.POST['first_name'], 
    last_name = request.POST['last_name'], email = request.POST['email'], age=request.POST['age'])
    context = {
        "all_users": users.objects.all()
    }
    return render(request, 'index.html', context)

def delete_dojo(request):
    deleting = dojos.objects.get(id = request.POST['dojo_delete'])
    deleting.delete()
    return redirect('/dojos')