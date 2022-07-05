from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Curso_forms(forms.Form):
    name    = forms.CharField(max_length=40)
    section = forms.IntegerField()

class Cadetes_forms(forms.Form):
  name = forms.CharField(max_length=40)
  lastname = forms.CharField(max_length=40)
  email = forms.EmailField()

class Instructor_forms (forms.Form):
  name = forms.CharField(max_length=40)
  lastname = forms.CharField(max_length=40)
  email = forms.EmailField()
  subject = forms.CharField(max_length=40)


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model     = User
        fields    = ['email', 'password1', 'password2']
        help_text = {k:"" for k in fields}