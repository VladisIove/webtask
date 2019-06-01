from django.urls import path 
from . import views 

app_name='post'

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('<slug:category_slug>', views.post_list, name='post_list_by_category'),
	path('<int:id>/<slug:slug>/', views.post_detail, name='post_detail'),
	path('search/', views.seacrch_post, name='search'),
	path('like/<int:id_post>/', views.like_post, name='like'),
	path('like_post_list/<int:id_post>/', views.like_post_list, name='like_post_list'),
	path('comment/<int:id>/', views.add_comment_to_post, name='add_comment_to_post'),
]