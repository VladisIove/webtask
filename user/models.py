from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True, null=True)
	username = models.CharField(max_length=200)
	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
		)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. ''Unselect this instead of deleting accounts.'
			),
		)

	USERNAME_FIELD = 'email'
	objects = CustomUserManager()
	birthday = models.DateField(auto_now_add=False, blank=True, null=True)
	country = models.CharField(max_length=120, blank=True, null=True)
	city = models.CharField(max_length=120, blank=True, null=True)

	def email_user(self, subject, message, from_email=None, **kwargs):

		send_mail(subject, message, from_email, [self.email], **kwargs)
