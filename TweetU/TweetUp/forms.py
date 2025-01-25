from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your tweet here...',
                'rows': 3
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                
                'placeholder': 'Enter a username',
                 'class':'textarea form-control tiny-editor'
            }),
            'password1': forms.PasswordInput(attrs={
               
                'class': 'form-control',
                'placeholder': 'Enter a password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password'
            }),
        }
