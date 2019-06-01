from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

	def create_user(self, email_user, password=None, **kwargs):
		if not email_user:
			raise ValueError('Email field is required')
		email_user = self.normalize_email(email_user)
		user = self.model(email_user=email_user, **kwargs)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email_user, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)
		return self.create_user(email_user, password, **extra_fields)

