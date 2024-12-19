from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request,'home/home.html')

@login_required
def register(request):
    return render(request,'home/register.html')

@login_required
def tournaments(request):
    return redirect('/register')
    # return render(request,'home/tournaments.html')

@login_required
def achievements(request):
    messages.error(request,'No match Played yet ! Register Now ..')
    return redirect('/register')
    # return render(request,'home/achievements.html')

@login_required
def games(request):
    messages.error(request,'No Games Played yet ! Register Now ..')
    return redirect('/register')
    # return render(request,'home/games.html')

def rules(request):
    return render(request,'home/rules.html')

def aboutus(request):
    return render(request,'home/aboutus.html')

def partners(request):
    return render(request,'home/partners.html')

def contactus(request):
    return render(request,'home/contactus.html')

def privacypolicy(request):
    return render(request,'home/privacypolicy.html')

def termsofservice(request):
    return render(request,'home/termsofservice.html')

def refundpolicy(request):
    return render(request,'home/refundpolicy.html')

def error_404_view(request, exception):
    return render(request, 'home/404.html', status=404)

def error_500_view(request):
    return render(request, 'home/500.html', status=500)