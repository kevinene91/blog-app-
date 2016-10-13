from django.contrib.auth import (
	get_user_model,
	authenticate, 
	login, 
	logout, 


	)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 

from .forms import UserLoginForm, UserRegisterForm

from .forms import UserLoginForm

# Create your views here.

def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None )
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/")

	return render(request, "form.html", {"form": form, "title": title})


def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)

		login(request, new_user)
		return redirect("/")

	context = {
		"title": title, 
		"form": form, 
	}
	return render(request, "form.html", context)

@login_required(login_url='/login/')
def logout_view(request):
	logout(request)
	return redirect("/")
	return render(request, "form.html", {})





