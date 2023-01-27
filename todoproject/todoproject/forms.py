from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(label='Message')
    sender = forms.EmailField(label='Email')
    cc_myself = forms.BooleanField(required=False)