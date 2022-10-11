from django import forms
from .models import OrderAnimal, AddModelAnimal
from animal.models import Animals, Category



class OrderForm(forms.ModelForm):

    class Meta:
        model = OrderAnimal
        fields = ['email', 'phone_number', 'last_name', 'first_name', 'animal', 'category', 'body',]
        exclude = ('status',)

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        animal: forms.ModelChoiceField(queryset=Animals.objects.all())
        category: forms.ModelChoiceField(queryset=Category.objects.all())

class ModelForm(forms.ModelForm):

    class Meta:
        model = AddModelAnimal
        fields = ['email', 'phone_number', 'last_name', 'first_name', 'pets_name', 'weight', 'height', 'color', 'descriptions', 'photo']
        exclude = ('status',)

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pets_name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(),
        }