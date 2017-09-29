from django import forms


class Sign_in_forms(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    pw= forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)


class Register_forms(forms.Form):
    name = forms.CharField(label="First Name", max_length=50)
    username = forms.CharField(label="Username", max_length=50)
    pw = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
    confpw = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
