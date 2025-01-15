from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
import requests
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *

def home(request):
    return render(request,'home/home.html')

@login_required
def register(request):
    return render(request,'home/register.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            if Team.objects.filter(user=request.user).exists():
                messages.error(request, 'Your team is already created!')
                return redirect('/profile')  # Redirect back to the profile page
            team = form.save(commit=False)
            team.user = request.user
            team.save()
            messages.success(request,'Your Team has been registered successfuly! Be ready for the Arena.')
            return redirect('/profile')  # Replace with your desired redirect
    else:
        form = TeamForm()
    team = None
    if Team.objects.filter(user=request.user).exists():
        team = Team.objects.filter(user=request.user).first()
    context = {'form':form, 'team':team}
    return render(request,'home/profile.html', context)


@login_required
def add_phone_number(request):
    if request.method == 'POST':
        print('post')
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            request.user.phone_number = phone_number
            request.user.save()
            messages.success(request, "Phone number added successfully!")
            return redirect('/register')  # Redirect to the profile or appropriate page
        else:
            messages.error(request, "Please enter a valid 10-digit phone number.")
            return redirect('/register')  # Redirect to the profile or appropriate page
    else:
        return redirect('/register')


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

@login_required
def payment_view(request):
    key = "6d125189-6290-4f37-bac8-5b7cafa0d353"
    client_txn_id = str(random.randint(100000, 999999))
    amount = '500'
    customer_name = request.user.first_name
    customer_email = request.user.email
    customer_mobile = f'{request.user.phone_number}'
    redirect_url = "https://playesports.in/verify-payment/"

    # Save a new Payment record with status pending
    payment = Payment.objects.create(
        user=request.user,
        client_txn_id=client_txn_id,
        amount=amount,
        status="pending",
    )

    post_data = {
        "key": key,
        "client_txn_id": client_txn_id,
        "amount": amount,
        "p_info": "BGMI Tournament",
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_mobile": customer_mobile,
        "redirect_url": redirect_url,
        "udf1": "extradata",
        "udf2": "extradata",
        "udf3": "extradata",
    }
    print(post_data)

    response = requests.post(
        'https://api.ekqr.in/api/create_order',
        json=post_data,
        headers={'Content-Type': 'application/json'}
    )
    result = response.json()

    if result.get('status'):
        messages.success(request, 'Payment Initiated Successfully!')
        return redirect(result['data']['payment_url'])
    else:
        # Update payment status to failure
        payment.status = "failure"
        payment.save()
        return JsonResponse({'error': result.get('msg')}, status=400)

@csrf_exempt
def callback_view(request):
    if request.method == 'POST':
        data = request.POST
        status = data.get('status')
        client_txn_id = data.get('client_txn_id')

        # Update payment status in the database
        try:
            payment = Payment.objects.get(client_txn_id=client_txn_id)
            payment.status = status
            payment.save()

            if status == "success":
                messages.success(request,"Transaction Successful")
            elif status == "failure":
                messages.error(request,"Transaction Failed")
            else:
                messages.error(request,"Unknown Transaction status")
        except Payment.DoesNotExist:
            messages.error(request,"Payment Not Found.")
    messages.error(request,"Invalid Request.")
    return redirect('/register')


@login_required
def redirect_page_view(request):
    client_txn_id = request.GET.get('client_txn_id')
    key = "6d125189-6290-4f37-bac8-5b7cafa0d353"  # Your API Token
    txn_date = "dd-mm-yyyy"  # Replace with the transaction date

    post_data = {
        "key": key,
        "client_txn_id": client_txn_id,
        "txn_date": txn_date
    }

    response = requests.post(
        'https://api.ekqr.in/api/check_order_status',
        json=post_data,
        headers={'Content-Type': 'application/json'}
    )

    result = response.json()
    txn_data = result.get('data', {})

    # Redirect to a profile page after handling the result
    messages.success(request,'Congratulations ! You are Registered for the BGMI Tournament on 25, Being the team leader fill your team details.')
    return redirect('/profile')


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

def ads_txt(request):
    ads_txt_content = """google.com, pub-5564090407790217, DIRECT, f08c47fec0942fa0"""
    return HttpResponse(ads_txt_content, content_type='text/plain')
