from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(min_length=1, max_length=3000, required=False)
    due_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    status = forms.BooleanField(required=False)