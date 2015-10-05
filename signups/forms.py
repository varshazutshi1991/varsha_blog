from django.forms import ModelForm

from signups.models import SignUp

class SignUpForm(ModelForm):
	class Meta:
		model = SignUp
		fields = ['first_name', 'last_name', 'email']
