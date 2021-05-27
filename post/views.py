from django.shortcuts import render, redirect
import requests
from .models import User
from .models import Job
from .models import City
from .forms import CityForm
from django.contrib import messages

def weather(request):
    url = 'http://api.openweathermap.org./data/2.5/weather?appid=0b634b858dce0e6dc5b6c3b66470bf02&units=metric&q='
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    if cities:
        for city in cities:
            data_url = url + str(city)
            response = requests.get(data_url).json()
            city_weather = {
                'city': city.name,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
    return render(request, 'weather.html', {'weather_data': weather_data, 'form': form})

def home(request):
        users=User.objects.all()
        return render(request, 'home.html',{'users':users})

def add(request):
    jobs=Job.objects.all()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        User.objects.create(firstname=firstname, lastname=lastname, age=age)
        messages.success(request, 'User has been added')
    return render(request, 'add.html', {'jobs':jobs})

def update(request,id):
    user=User.objects.get(id=id)
    jobs=Job.objects.all()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        User.objects.filter(id=id).update(firstname=firstname, lastname=lastname, age=age)
        messages.success(request, 'User has been updated')
    return render(request, 'update.html',{'user':user, 'jobs':jobs})

def delete(request,id):
    User.objects.filter(id=id).delete()
    return redirect('/')


def job(request):
        jobs=Job.objects.all()
        return render(request, 'job.html',{'jobs':jobs})

def addjob(request):
    if request.method=='POST':
        name=request.POST['name']
        Job.objects.create(name=name)
        messages.success(request, 'Job has been added')
    return render(request, 'addjob.html')

def updatejob(request,id):
    job=Job.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        Job.objects.filter(id=id).update(name=name)
        messages.success(request,'Job has been updated')
    return render(request, 'updatejob.html',{'job':job})

def deletejob(request,id):
    Job.objects.filter(id=id).delete()
    return redirect('/job')