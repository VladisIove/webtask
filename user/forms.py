from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django_registration.forms import RegistrationForm ,RegistrationFormUniqueEmail

from .models import User 


class CustomUserForm(RegistrationFormUniqueEmail):

	class Meta():
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'country', 'city', 'birthday')