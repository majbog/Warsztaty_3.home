from django import forms

from .models import CONTACT_TYPES



class AddPhoneForm(forms.Form):
    number = forms.IntegerField()
    type = forms.ChoiceField(choices=CONTACT_TYPES)
    contact_person = forms.IntegerField(widget=forms.HiddenInput)


class AddMailForm(forms.Form):
    address = forms.EmailField()
    type = forms.ChoiceField(choices=CONTACT_TYPES)
    contact_person = forms.IntegerField(widget=forms.HiddenInput)
