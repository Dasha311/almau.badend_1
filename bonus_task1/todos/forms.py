from django import forms


#class CreateTodoForm(forms.Form):
    #title = forms.CharField(min_length=1, max_length=255, required=True)
    #description = forms.CharField(min_length=1, max_length=3000, required=False)
    #due_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    #status = forms.BooleanField(required=False)
    #todo_list = forms.ForeignKey(required=False)

class CreateTodoForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}))
    description = forms.CharField(min_length=0, max_length=3000, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description'}))
    due_date = forms.DateField(min_value=1, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product amount'}))
    status = forms.BooleanField( required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))