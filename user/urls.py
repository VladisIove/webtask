from django.urls import path 

from django_registration.backends.activation.views import RegistrationView

from . import views 
from .models import User
from .forms import CustomUserForm
app_name='user'

urlpatterns = [
	path('register/', RegistrationView.as_view(form_class=CustomUserForm), name='registration_register'),
]