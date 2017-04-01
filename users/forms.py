from django import forms
from django.contrib.auth import ( authenticate, get_user_model )

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		
		user_qs = User.objects.filter(username=username)
		if user_qs.count() == 0:
			raise forms.ValidationError("This user does not exist!")
		else:
			user = authenticate(username=username, password=password)
			
			if not user:
				raise forms.ValidationError("Incorrect password!")

			if not user.is_active:
				raise forms.ValidationError("This user is no longer active!")

		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	email_confirm = forms.EmailField(label='Confirm Email')
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email_confirm',
			'password',
			'password_confirm'
		]

	def clean_email_confirm(self):
		email = self.cleaned_data.get('email')
		email_confirm = self.cleaned_data.get('email_confirm')

		if email != email_confirm:
			raise forms.ValidationError("Emails must match!")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered!")

		return email

	def clean_password_confirm(self):
		password = self.cleaned_data.get('password')
		password_confirm = self.cleaned_data.get('password_confirm')

		if password != password_confirm:
			raise forms.ValidationError("Passwords must match!")

		return password