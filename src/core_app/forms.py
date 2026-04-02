from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ad

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True, label='Email')
	username = forms.CharField(max_length=30, required=True, label='Username')

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email')


class AdForm(forms.ModelForm):
	class Meta:
		model = Ad
		fields = ['category', 'city', 'image', 'title', 'description', 'price']
		widgets = { 'description': forms.Textarea(attrs={'rows': 4}) }