from django import forms

class GCRequestForm(forms.Form):
    description=forms.CharField(max_length=200,widget=forms.Textarea)
    image=forms.ImageField()
    latitude=forms.DecimalField(min_value=-90,max_value=90,max_digits=15, decimal_places=10,widget=forms.HiddenInput())
    longitde=forms.DecimalField(min_value=-180,max_value=180,max_digits=15, decimal_places=10,widget=forms.HiddenInput())
