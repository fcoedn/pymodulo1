from django import forms

Class SubscriptionForm(forms.Forms):
    name = forms.CharField()
    cpf = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
