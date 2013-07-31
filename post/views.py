from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
	return render_to_response('home.html', {'posts':posts}, context_instance=RequestContext(request))

def sign_up(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		passwordc = request.POST['passwordc']
		if sorted(password) == sorted(passwordc):
			if User.objects.filter(username=username).count()==0:
				user = User.objects.create(username=username)
				user.set_password(password)
				user.save()
				msgOk = 'User created.'
				access = authenticate(username=username, password=password)
				login(request, access)
				return render_to_response('sign_up.html', {'msgOk':msgOk}, context_instance=RequestContext(request))
			else:
				msgError = 'Username invalid.'
				return render_to_response('sign_up.html', {'msgError':msgError}, context_instance=RequestContext(request))
		else:
			msgError = 'Password confirmation invalid.'
			return render_to_response('sign_up.html', {'msgError':msgError}, context_instance=RequestContext(request))
	return render_to_response('sign_up.html', context_instance=RequestContext(request))

def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		access = authenticate(username=username, password=password)
		if access is not None:
			login(request, access)					
			return HttpResponseRedirect('/')
		else:
			msgError = 'User or password incorret'
			return render_to_response('log_in.html',{'msgError':msgError}, context_instance=RequestContext(request))
	else:
		return render_to_response('log_in.html', context_instance=RequestContext(request))

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')