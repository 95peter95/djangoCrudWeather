from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('job',views.job,name='job'),
    path('addjob',views.addjob,name='addjob'),
    path('updatejob/<int:id>',views.updatejob,name='updatejob'),
    path('deletejob/<int:id>',views.deletejob,name='deletejob'),
    path('weather',views.weather,name='weather'),
]