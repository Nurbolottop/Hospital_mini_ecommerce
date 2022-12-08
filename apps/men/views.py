from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.settings.models import Settings
from apps.contact.models import Contacts,Contact_detail
from apps.men.models import Men

# Create your views here.
def men(request):
    men = Men.objects.all()

    setting = Settings.objects.latest('id')
    contacts = Contacts.objects.latest('id')
    if request.method  == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact_detail.objects.create(name = name,email = email,message = message)
        send_mail(
            f"{message}",
            f"Hello {name}, Thank you for your response, we will contact you shortly. Your message: {message} Your E-mail: {email}",
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')

    context = {
        'setting':setting,
        'contacts':contacts,
        'men':men,
        
    }

    return render(request, 'men.html', context)


def men_detail(request, id):
    mens = Men.objects.get(id =id)


    setting = Settings.objects.latest('id')
    contacts = Contacts.objects.latest('id')

    context = {
        'setting':setting,
        'contacts':contacts,
        'mens':mens,
        
    }

    return render(request, 'men_detail.html', context)
