from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.settings.models import Settings,Slide,Men,Women,Banner,Contacts,Contact_detail


# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    men = Men.objects.all()
    women = Women.objects.all()
    banner = Banner.objects.latest('id')
    contacts = Contacts.objects.latest('id')
    if request.method  == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact_detail.objects.create(name = name,email = email,message = message)
        send_mail(
            f"{message}",
            # message:
            f"Hello {name}, Thank you for your response, we will contact you shortly. Your message: {message} Your E-mail: {email}",
            # from:
            "noreply@somehost.local",
            # to:
            [email]
            
        )
        return redirect('index')

    context  = {
        'setting':setting,
        'slide':slide,
        'men':men,
        'women':women,
        'banner':banner,
        'contacts':contacts,

    }

    return render(request, 'index-3.html', context)