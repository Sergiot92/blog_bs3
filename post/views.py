from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from post.models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	posts = Post.objects.all().order_by('-creation_date')
	paginator = Paginator(posts, 5)
	try:
		page = request.GET['page']
		posts = paginator.page(page)	
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	except Exception:
		posts = paginator.page(1)
	return render_to_response('home.html',{'posts':posts}, context_instance=RequestContext(request))

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')