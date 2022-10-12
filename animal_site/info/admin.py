from django.contrib import admin
from .models import Info, Questions, Answers, SocialMedia, PriceList

admin.site.register(Info)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(SocialMedia)
admin.site.register(PriceList)