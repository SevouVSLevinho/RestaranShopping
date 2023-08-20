from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	email = forms.EmailField(max_length=254, help_text='eg. youremail@anyemail.com')

	class Meta:
		model = User
		fields = ('first_name','last_name','email','username','password1','password2')

	captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

# class SetPasswordForm(SetPasswordForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['new_password1', 'new_password2']

# class PasswordResetForm(PasswordResetForm):
#     def __init__(self, *args, **kwargs):
#         super(PasswordResetForm, self).__init__(*args, **kwargs)

#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())