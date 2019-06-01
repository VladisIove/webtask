from datetime import timezone

from django.db import models
from django.conf import settings

from django.urls import reverse 

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ('name', )

	def get_absolute_url(self):
		return reverse('post:post_list_by_category', args=[self.slug])

	def __str__(self):
		return self.name 

class Post(models.Model):
	category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=120, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)
	body = models.TextField()
	image = models.ImageField(upload_to='img_post')


	

	class Meta:
		ordering = ('title', )
		index_together = (('id', 'slug'),)
		
	def get_absolute_url(self):
		return reverse('post:post_detail', args=[self.id, self.slug])


	def __str__(self):
		return self.title 

class Comment(models.Model):
	post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey('user.User', on_delete=models.CASCADE )
	text = models.TextField()

	def __str__(self):
		return self.text


class Like(models.Model):
	user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
	post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
	creation_date = models.DateTimeField(auto_now=True)



