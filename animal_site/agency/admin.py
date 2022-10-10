from django.contrib import admin
from .models import AddModelAnimal, OrderAnimal


admin.site.register(AddModelAnimal)
admin.site.register(OrderAnimal)