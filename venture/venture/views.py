from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django import template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from member.models import MyUser
import json
# Create your views here.

def login(request):
	if not request.user.is_authenticated():
		if request.POST:
			if request.user.is_authenticated():
				return HttpResponseRedirect('/index')
			else:

				username = request.POST['username']
				password = request.POST['password']

				user = auth.authenticate(username=username,password=password)

				if user is not None and user.is_active:
					auth.login(request,user)
					return HttpResponseRedirect('/index/')
				else:
					return render_to_response('login.html', RequestContext(request,locals()))
		else:
			return render_to_response('login.html', RequestContext(request,locals()))
	else:
		return HttpResponseRedirect('/index/')

def index(request):	
	users= MyUser.objects.all()
	usersname=[]
	for user in users:
		usersname.append(user.get_username)
	if request.user.is_authenticated():
		username= request.user.get_username()
	return render_to_response('index.html', RequestContext(request,locals()))

def logout(request):
	auth.logout(request)
	if 'user' in request.session:
		del	request.session['user']
	return HttpResponseRedirect('/index/')

def register(request):
	if request.POST:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			newuser = form.save()			
			return HttpResponseRedirect('/accounts/login')
	else:
		form = UserCreationForm()
	return render_to_response('register.html', RequestContext(request,locals()))
