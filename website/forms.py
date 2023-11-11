from django import forms
from website.models import contact, Newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm) :
    # age = forms.IntegerField()
    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'message']
        # fields = '__all__'
        # fields = ['name', 'email'] or exclude = ['something'] and ...
        # widgets = ...

class NewsletterForm(forms.ModelForm) :
    class Meta :
        model = Newsletter
        fields = '__all__'