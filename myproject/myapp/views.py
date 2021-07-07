from django.shortcuts import get_object_or_404, render
from .models import Mail


def home(request):
    mails = Mail.objects
    return render(request, 'home.html', {'mails': mails})
# Create your views here.


def detail(request, mail_id):
    mail_detail = get_object_or_404(Mail, pk=mail_id)
    return render(request, 'detail.html', {'mail': mail_detail})
