from django.shortcuts import render

from apps.settings.models import Settings,Slide,Men,Women

# Create your views here.

def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    men = Men.objects.all()
    women = Women.objects.all()

    context  = {
        'setting':setting,
        'slide':slide,
        'men':men,
        'women':women,

    }

    return render(request, 'index-3.html', context)