from django import forms

from phonenumber_field.formfields import PhoneNumberField


STATUS_CHOICES = (
    (True, 'Active'),
    (False, 'Inactive'))


class UserForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=64)
    phone = PhoneNumberField(required=False)
    mobile = PhoneNumberField(required=False)

    status = forms.ChoiceField(choices=STATUS_CHOICES)
