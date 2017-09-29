from django import forms

TRAVEL_CHOICES = ('2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025')
class Travel(forms.Form):
    destination = forms.CharField(label="Destination", max_length=100)
    description = forms.CharField(label="Description", max_length=250)
    traveldate_from = forms.DateField(label="Travel Date From", widget=forms.SelectDateWidget(years=TRAVEL_CHOICES))
    traveldate_to = forms.DateField(label="Travel Date To", widget=forms.SelectDateWidget(years=TRAVEL_CHOICES))