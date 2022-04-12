from django import forms

from registration.main.models import Contact, FeedBack


# First Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('user',)


class LeaveFeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        exclude = ('user',)
        widgets = {
            'status': forms.RadioSelect()
        }
