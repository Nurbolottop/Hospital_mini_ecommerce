from django.contrib import admin

from apps.settings.models import Settings,Slide,Men,Women,Banner,Contacts,Contact_detail

# Register your models here.

admin.site.register(Settings)
admin.site.register(Slide)
admin.site.register(Men)
admin.site.register(Women)
admin.site.register(Banner)
admin.site.register(Contacts)
admin.site.register(Contact_detail)

