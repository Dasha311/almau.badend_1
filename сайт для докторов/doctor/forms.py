from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Appointment

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CreateDoctorForm(forms.Form):
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

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialty', 'experience_years', 'bio', 'profile_picture']
        widgets = {
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter doctor specialty'}),
            'experience_years': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter years of experience'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter biography'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'appointment_reason', 'status']

    # Дополнительные поля для формы, если необходимо кастомизировать
    patient = forms.ModelChoiceField(queryset=User.objects.all(), label='Patient')
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label='Doctor')
    appointment_date = forms.DateField(label='Appointment Date')
    appointment_time = forms.TimeField(label='Appointment Time')
    appointment_reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Reason for Appointment')
    status = forms.ChoiceField(choices=Appointment.status_choices, label='Status')