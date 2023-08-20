from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from order.models import Profile

class EditProfileForm(forms.ModelForm):
	picture = forms.ImageField(required=False)
	first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
	last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
	location = forms.CharField(widget=forms.TextInput(), max_length=25, required=False)
	url = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
	profile_info = forms.CharField(widget=forms.TextInput(), max_length=150, required=False)

	class Meta:
		model = Profile
		fields = ('picture', 'first_name', 'last_name', 'location', 'url', 'profile_info')
