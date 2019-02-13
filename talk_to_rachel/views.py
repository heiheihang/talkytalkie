from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
import datetime
from .models import Post
from .forms import PublishPost, TestForm
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect


class Index(generic.ListView):
    model = Post
def past_posts(request):
    current_time = datetime.datetime.now()
    filtered_posts = Post.objects.all()
    if filtered_posts.count() == 0:
        return HttpResponseRedirect(reverse('test'))
    else:
        context = {
            'posts' : filtered_posts
        }
        return render(request, 'past_posts.html', context=context)

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	template = loader.get_template('talk_to_rachel/index.html')
	context = {
		'latest_post_list' : latest_post_list
	}
	return render(request, 'talk_to_rachel/index.html', context)
# Create your views here.

def post_detail(request, post_id):

	post = get_object_or_404(Post, pk=post_id)

	return render (request, 'talk_to_rachel/detail.html', {'post' : post})

def add_post(request):
	if request.method== 'POST':
		retrieved_post = PublishPost(request.POST)
		if retrieved_post.is_valid():
			form_post_title = retrieved_post.cleaned_data['post_title']
			form_post_content = retrieved_post.cleaned_data['post_content']
			form_post_publish_date = timezone.now()

			new_post = Post(post_title = form_post_title, post_content=form_post_content, pub_date = form_post_publish_date)
			new_post.save()

			return HttpResponseRedirect(reverse('test'))
	context = {
		'form' : PublishPost,
	}
	return render(request, 'publish_post.html', context=context)

def testing(request):
    current_time = datetime.datetime.now()

    filtered_posts = Post.objects.all()
    post_count = filtered_posts.count()
    if post_count >= 3:
        filtered_posts = filtered_posts[:3]
        post_count = 3


    
    context = {
        'posts' : filtered_posts,
    }

    return render(request, 'test.html', context = context)

class PostDetailView(generic.DetailView):
	model = Post
	def post_detail_view(request, primary_key):
		post = get_object_or_404(Post, pk=primary_key)
		return render(request, 'talk_to_rachel/post_detail.html', context={'post':post})