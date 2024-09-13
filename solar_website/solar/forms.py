from django import forms
from .models import ContactForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'class' : 'form-control'}),
            'subject': forms.TextInput(attrs={'class' : 'form-control col-12'}),
            'message': forms.Textarea(attrs={'class' : 'form-control'}),
        }