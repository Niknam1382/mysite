from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth.decorators import login_required
import random

from accounts.forms import UserForm
from django.contrib.auth.models import User

from django.conf import settings
from django.core.mail import EmailMessage , send_mail

from django.contrib import messages
import re

# Create your views here.
def login_view(request):
    '''
    if request.user.is_authenticated:
        msg = f'user is authenticated as {request.user.username}'
    else:
        msg = 'user is not authenticated'
    '''
    '''
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.filter(email=email).first()
        if email:
            username = user.username
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            response = redirect('/') # redirect to main page
            return response
        else:
            pass
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)  #{'msg':msg}
    '''
    msg = None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if the username is an email address
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
            email = username
            user = User.objects.filter(email=email).first()
            if user:
                username = user.username

            user = authenticate(request, username=username, password=password)
        else:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = messages.error(request, "User not found. Please try again.")
            pass

    form = AuthenticationForm()
    context = {'form': form, 'msg': msg}
    return render(request, 'accounts/login.html', context)
    '''
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else :
        return redirect('/')
'''
'''
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                if username:
                    user = authenticate(request, username=username, password=password)
                elif email:
                    user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
'''
@login_required
def logout_view(request):
# if request.user.is_authenticated:
    logout(request)
    return redirect('/') # redirect to the main page

'''
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # return redirect('acconuts/login/')
                # return reverse('acconuts/login')
                return redirect('/accounts/login')
            
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html',context)
    else:
        return redirect('/')
'''


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                email = data['email']
                password = data['password']
                first_name = data['first_name']
                last_name = data['last_name']
                confirm = request.POST.get('confirm')

                
                if not User.objects.filter(email = email) and password == confirm :

                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('/accounts/login')
                
                else :
                    msg = messages.warning(request, "passwords not match")
                    return render(request, 'accounts/signup.html',{'msg':msg})

        form = UserForm()
        return render(request, 'accounts/signup.html',{'form':form})
    else:
        return redirect('/')
    

'''
def reset_view(request) :
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_email = request.POST["email"]
            Email = request.POST["email"]
            Email = [str(Email)]
            number = random.randrange(10000000, 99999999)
            number = str(number)
            subject = 'reset password'
            message = 'Your Reset Password Code is : ' + number 
            email_from = settings.EMAIL_HOST_USER
            email = EmailMessage(subject, message, email_from, Email)
            email.send()
            send_mail(subject, message, email_from, Email)
            number = int(number)
            return redirect('/accounts/change-password')
        
        # if request.method == 'POST':
        #     password2 = request.POST["password"]
        #     confirm = request.POST["confirm"]
        #     if int(confirm) == number :

        #         u = User.objects.get(email=user_email)
        #         u.set_password(password2)
        #         u.save()


    return render(request, 'accounts/reset.html')

def change_password(request):
    if request.method == 'POST':
            password2 = request.POST["password"]
            confirm = request.POST["confirm"]
            if int(confirm) == number :

                u = User.objects.get(email=user_email)
                u.set_password(password2)
                u.save()
    return render(request, 'accounts/change.html')
'''
def reset_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_email = request.POST["email"]
            Email = request.POST["email"]
            Email = [str(Email)]
            number = random.randrange(10000000, 99999999)
            number = str(number)
            subject = 'reset password'
            message = 'Your Reset Password Code is : ' + number
            email_from = settings.EMAIL_HOST_USER
            email = EmailMessage(subject, message, email_from, Email)
            email.send()
            send_mail(subject, message, email_from, Email)
            
            request.session['user_email'] = user_email
            request.session['reset_code'] = number
            
            return redirect('/accounts/change-password')
    
    return render(request, 'accounts/reset.html')


def change_password(request):
    if request.method == 'POST':
        password2 = request.POST["password"]
        confirm = request.POST["confirm"]
        
        user_email = request.session.get('user_email')
        reset_code = request.session.get('reset_code')
        
        if confirm == reset_code:
            try:
                user = User.objects.get(email=user_email)
                user.set_password(password2)
                user.save()
                return redirect('/accounts/login')
            except User.DoesNotExist:
                return redirect('/accounts/reset-password')
    
    return render(request, 'accounts/change.html')