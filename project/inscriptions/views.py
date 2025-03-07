from django.shortcuts import render, redirect
from inscriptions.models import index
from .forms import indexForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def inscription_view(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            # Envoi de l'e-mail de confirmation
            message = render_to_string('email_confirmation.txt', {'participant': participant})
            send_mail(
                'Confirmation d\'inscription',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [participant.email],
            )
            return redirect('confirmation')
    else:
        form = ParticipantForm()
    return render(request, 'inscription.html', {'form': form})

def confirmation_view(request):
    return render(request, 'confirmation.html')

from django.contrib.auth.decorators import login_required

@login_required
def liste_participants_view(request):
    participants = Participant.objects.all()
    return render(request, 'liste_participants.html', {'participants': participants})

