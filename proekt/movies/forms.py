from django import forms
from django.contrib.auth.models import User
from .models import Movie


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CreateMovieForm(forms.Form):
    title = forms.CharField(
        min_length=1,
        max_length=200,
        required=True,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Enter movie title'
        })
    )
    description = forms.CharField(
        min_length=0,
        max_length=2000,
        required=False,
        widget=forms.Textarea({
            'class': 'form-control',
            'placeholder': 'Enter description'
        })
    )
    producer = forms.CharField(
        min_length=1,
        max_length=200,
        required=True,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Enter producer'
        })
    )
    duration = forms.IntegerField(
        min_value=0,
        required=True,
        label='Duration in minutes',
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Enter duration in minutes'
        })
    )


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter movie title'
            }),
            'producer': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter producer'
            }),
            'description': forms.Textarea({
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'duration': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter duration in minutes'
            }),
        }