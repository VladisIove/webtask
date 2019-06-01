from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST 

from .models import Category, Post,  Comment, Like
from .forms import SearchForm, CommentForm

from user.models import User
# Create your views here.

@login_required()
def post_list(request, category_slug=None):
	category = None 
	categories = Category.objects.all()
	posts = Post.objects.all()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		posts = posts.filter(category=category)

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	search = SearchForm()
	like = Like.objects.all()

	for post in page.object_list:
		post.likes = post.like_set.all().count()
	context = {'category': category, 
	'categories': categories, 
	'page_object': page,
	'next_url': next_url,
	'prev_url': prev_url,
	'search':search,
	'like': like
	}

	return render( request, 'posts/list.html', context)

@login_required()
def post_detail(request,id, slug ):
	post = get_object_or_404(Post, id=id, slug=slug)
	search = SearchForm()
	comment_form = CommentForm()
	comments = Comment.objects.filter(post=post)

	paginator = Paginator(comments, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	number_of_likes = post.like_set.all().count()

	context = {
		'post': post,
		'page_object': page,
		'next_url': next_url,
		'prev_url': prev_url,
		'search': search,
		'comment_form': comment_form ,
		'comments': comments,
		'count': number_of_likes
	}
	return render(request, 'posts/detail.html', context=context)



@require_POST
def like_post(request, id_post):
	post = get_object_or_404(Post, id = id_post)
	user = get_object_or_404(User, email=request.user)

	new_like, created = Like.objects.get_or_create(user=user, post=post)
	if not created:
		Like.objects.get(user=new_like.user, post=post).delete()
	

	return redirect('post:post_detail', str(post.id), post.slug)


@require_POST
def like_post_list(request, id_post):
	post = get_object_or_404(Post, id = id_post)
	user = get_object_or_404(User, email=request.user)

	new_like, created = Like.objects.get_or_create(user=user, post=post)
	if not created:
		Like.objects.get(user=new_like.user, post=post).delete()
	
		
	return redirect('post:post_list')

@require_POST
def seacrch_post(request):
	form = SearchForm( request.POST )

	if form.is_valid():
		search = form.cleaned_data['body']
		try:
			post = Post.objects.get(title=search) 
			return redirect('post:post_detail', post.id, post.slug)
		except:
			return redirect('post:post_list')
	else:
		return redirect('post:post_list')

@require_POST
def add_comment_to_post(request, id):
    post = get_object_or_404(Post, id=id)
    user = get_object_or_404(User, email=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(post = post, author = user, text = form.cleaned_data['body'])
            return redirect('post:post_detail', str(post.id), post.slug)
    else:
        form = CommentForm()
    return render(request, 'post/add_comment_to_post.html', {'form': form})

	