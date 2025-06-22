from django.shortcuts import render
from adminapp.models import *
from userapp.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def index(request):

    all_bio = profile_bio.objects.all()
    all_banner = banner.objects.all()
    all_skill = skills.objects.all()
    all_education = Education.objects.all()
    all_experience = Experience.objects.all()
    all_portfolio = Portfolio.objects.all()
    all_services = Services.objects.all()

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        contact = request.POST['contact']
        message_text = request.POST['message']

        contact_data = user_contact(
            name=name, 
            email=email, 
            subject=subject, 
            contact=contact, 
            message=message_text
        )
        contact_data.save()

        # send email
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Name: {name}\nEmail: {email}\nContact: {contact}\n\nMessage:\n{message_text}",
            from_email=email,
            recipient_list=['jaydeepkakadiya007@gmail.com'],  # where you want to receive the email
            fail_silently=False,
        )


        messages.success(request, "Your message has been sent successfully.")
        return redirect('index')
    
    return render(request, 'index.html', {'all_bio': all_bio, 'all_banner': all_banner , 'all_skill': all_skill , 'all_education': all_education , 'all_experience': all_experience , 'all_portfolio': all_portfolio , 'all_services': all_services})