from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


from .forms import FeedbackCreateForm
from .models import Feedback
from .utils import get_client_ip


def send_contact_email_message(name, phone, time, date):
    """
    Function to send contact form email
    """
    
    message = render_to_string('email/feedback_email_send.html', {
        'name': name,
        'phone': phone,
        'time': time,
        'date': date
    })
    subject = f"Заявка от {name}|{phone}"
    email = EmailMessage(subject, message, settings.EMAIL_SERVER, settings.EMAIL_ADMIN)
    email.send(fail_silently=False)


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'home/index.html'
    success_url = reverse_lazy('headapp:index')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            
            send_contact_email_message(feedback.name, feedback.phone, feedback.time, feedback.date)
        return super().form_valid(form)