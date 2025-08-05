from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Channel


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'terminal-input'


class ChannelCreateForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'terminal-input',
                'placeholder': 'Enter channel name...'
            })
        }


class ChannelJoinForm(forms.Form):
    channel_key = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'terminal-input',
            'placeholder': 'Enter channel key...'
        })
    )


class EncryptForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'terminal-input',
            'rows': 4,
            'placeholder': 'Enter message to encrypt...'
        })
    )


class DecryptForm(forms.Form):
    secret_key = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'terminal-input',
            'rows': 4,
            'placeholder': 'Enter secret key (comma-separated numbers)...'
        })
    )