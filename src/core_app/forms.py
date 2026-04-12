from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ad

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True, label='Email')

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class AdForm(forms.ModelForm):
	class Meta:
		model = Ad
		fields = ['title', 'category', 'city', 'description', 'price', 'image']
		widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Что вы продаете?',
                'required': True
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'city': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }