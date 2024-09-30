from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def homePage(request):
    return render(request, 'solar/home.html' )

def aboutPage(request):
    return render(request, 'solar/about.html')

def servicesPage(request):
    return render(request, 'solar/services.html')

def contactPage(request):
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender_email = form.cleaned_data['email']
            subject = f"Contacting goldlite: {form.cleaned_data['subject']}"
            message = f"Name: {form.cleaned_data['name']}\n Email:{form.cleaned_data['email']}\nMessage:{form.cleaned_data['message']}"
            try:
             send_mail(subject, message, sender_email, ['lightofor@gmail.com'],fail_silently = False)
             messages.success(request, "Email sent sucessfully")
             return redirect('home')
            except:
                messages.error(request, "Couldn't send email")
                
            
           

    else:
        form = ContactForm()
    return render(request,'solar/contact.html',{'form':form,})

def projectsPage(request):
    return render(request, 'solar/projects.html')

