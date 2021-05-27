from django.forms import ModelForm, TextInput
from .models import City
from .models import Job

class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'For example Zvolen'})}