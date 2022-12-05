from django.shortcuts import render

from apps.settings.models import Settings,Slide,Men,Women,Banner,Contacts


# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    men = Men.objects.all()
    women = Women.objects.all()
    banner = Banner.objects.latest('id')
    contacts = Contacts.objects.latest('id')

    context  = {
        'setting':setting,
        'slide':slide,
        'men':men,
        'women':women,
        'banner':banner,
        'contacts':contacts,

    }

    return render(request, 'index-3.html', context)