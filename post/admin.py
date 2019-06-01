from django.contrib import admin
from .models import Category, Post,Comment, Like
# Register your models here.

class CategoryAdmin( admin.ModelAdmin ):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', )}

class PostAdmin( admin.ModelAdmin ):
	list_display = ['category','title','slug','body','image', ]
	prepopulated_fields = {'slug': ('title', )}

class CommentAdmin( admin.ModelAdmin ):
	list_display = ['post','author','text']




admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
