from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def SignUpPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account Successfully created for '+user)
			return redirect('Login')
		else:
			print('wrong form')
	context = {'form':form}
	return render(request,'Account/signup.html',context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('HomePage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username=username,password=password)

			if user is not None:
				login(request, user)
				return redirect('HomePage')
			else:
				messages.info(request, 'Username or Password is Incorrect')
				return render(request, 'Account/login.html')

	context={}
	return render(request,'Account/login.html',context)


def logoutPage(request):
	logout(request)
	return redirect('Login')
