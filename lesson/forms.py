from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

choices = (('A1', 'A1'),
            ('A2', 'A2'),
            ('B1', 'B1'),
            ('B2', 'B2'),
            ('C1', 'C1'),
            ('native','native'),
           )


class RegistrationForm(UserCreationForm):
    languagelevel = forms.ChoiceField(choices=choices, label="German language level" ,help_text='Language level according to CEFR ->')
    native = forms.ChoiceField(choices=settings.LANGUAGES, label="Native language")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    source = forms.CharField(max_length=254, required=False, label="Where have you heard about this site?")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'languagelevel', 'native', 'source']
