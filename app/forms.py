from django import forms

class EmpAppForm(forms.Form):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': 'form-control'}))

# for later :)
class ConForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    note = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
