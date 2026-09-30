from django import forms
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',
                  'password1', 'password2']