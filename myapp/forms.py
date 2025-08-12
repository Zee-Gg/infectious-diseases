from django import forms

class HotspotForm(forms.Form):
    county = forms.CharField(label="County")
    year = forms.IntegerField(label="Year")
    sex = forms.ChoiceField(label="Sex", choices=[("M", "Male"), ("F", "Female")])
    population = forms.IntegerField(label="Population")
    count = forms.IntegerField(label="Disease Count")
