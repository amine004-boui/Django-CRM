from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have authenticated successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password, please try again...')
            return redirect('home')
    else:
        return render(request, 'website/home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'website/register.html', {'form':form})

	return render(request, 'website/register.html', {'form':form})
