from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
'''def home(request):
	return render(request, 'home.html')'''


def user_logout(request):
    logout(request)
    return redirect('/')