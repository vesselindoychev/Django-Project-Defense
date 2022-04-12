# First Contact
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render

from registration.main.forms.contact import ContactForm, LeaveFeedBackForm


@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}, Subject:{form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            context = {
                'form': form,
            }
            return render(request, 'main/success.html', context)
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)


@login_required
def leave_feedback(request):
    if request.method == 'POST':
        form = LeaveFeedBackForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            # email_status = f'You have rated your experience with {form.cleaned_data["status"]}'
            email_topic = f'Contact {form.cleaned_data["email"]} left FeedBack about {form.cleaned_data["topic"]} ' \
                          f'and rated his/her experience with {form.cleaned_data["status"]}'
            email_message = form.cleaned_data["message"]
            send_mail(email_topic, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            context = {
                'form': form,
            }
            return render(request, 'main/success-feedback-page.html', context)
    form = LeaveFeedBackForm()
    context = {
        'form': form,
    }

    return render(request, 'main/feedback-page.html', context)
