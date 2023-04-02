
from django import forms

class CreateNewTask(forms.Form):
    tittle = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label = 'Descripcion de la tarea' ,widget=forms.Textarea)
#Endclass

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Name project', max_length=200)
#Endclass