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