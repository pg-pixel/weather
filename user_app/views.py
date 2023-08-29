##########
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
##########
from .forms import CustomRegisterForm
##########
from lookup import views as lookup_app
##########

# Create your views here.

def register(request):
    if request.method == 'POST':
        registration_form = CustomRegisterForm(request.POST) 
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, ('User added Successfully! Kindly check Whatsapp to get started...'))
            print(registration_form.cleaned_data['phone_number'],{})
            lookup_app.Application_logic.send_whatsapp_msg(registration_form.cleaned_data['phone_number'],{})
            return redirect('Home') 
    else:
        registration_form = CustomRegisterForm()
        
    return render(request, 'register.html', {'registration_form':registration_form})