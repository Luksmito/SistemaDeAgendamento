from django.shortcuts import render
from .forms import ScheduleForm
from django.core.mail import send_mail
from .models import Schedule
from django.http import HttpResponse
import os
import dotenv
# Create your views here.

def schedulingForm(request):
    """
    View to render schedule template and verify the data 
    """
    available_schedules = Schedule.search_for_available_dates(Schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save(commit=False) 
            date_validation = form.verify_date()
            if not date_validation['valid']:
                context = {
                    'form': form, 
                    'date_error': date_validation['message'], #Inform to template if the date has already been scheduled
                    'available_schedules': available_schedules
                }
                return render(request, 'schedulingView.html', context)
            else: 
                schedule = form.save()
                context = {
                        'form': form, 
                        'success': 'success', #Inform to template if the schedule has been saved with success
                        'available_schedules': available_schedules
                    }
                try:
                    email = {
                        'subject': "Agendamento",   
                        'destiny': [schedule.email],
                        'message': f"Olá {schedule.name} seu agendamento ocorreu com sucesso, se quiser nos contactar use o telefone (XX)XXXXX-XXXX"
                    }
                    send_mail(email['subject'], email['message'], os.getenv("EMAIL_HOST_USER"), recipient_list = email['destiny']) 
                    print("email enviado")
                except ValueError as ve:
                    print(f"email nao enviado {ve}")
                return render(request, 'schedulingView.html', context)
        else:
            return render(request, 'schedulingView.html', {'form': form})
    else:
        form = ScheduleForm()
        context = {
            'form': form,
            'available_schedules': available_schedules
        }
        return render(request, 'schedulingView.html', context)

def teste(request):
    lista = Schedule.search_for_available_dates(Schedule)
    print(lista)
    return HttpResponse(lista)