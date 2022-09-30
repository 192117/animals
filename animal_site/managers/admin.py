from django.contrib import admin
from .models import Manager, FunctionsMixin

admin.site.register(Manager)
admin.site.register(FunctionsMixin)