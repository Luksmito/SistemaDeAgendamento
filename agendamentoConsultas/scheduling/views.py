from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import status

from .models import Schedule
from .forms import ScheduleForm
from .serializers import ScheduleSerializer

import os

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('date')
    serializer_class = ScheduleSerializer
    authentication_classes = [BasicAuthentication]
    
    def create(self, request, *args, **kwargs):
        """
        Method that controll thepost of a schedule
        """
        form = ScheduleForm(request.POST)
        #verify is form is valid
        if form.is_valid():
            #Verify if date is valid
            form.save(commit=False) 
            date_validation = form.verify_date()
            if not date_validation['valid']:
                return Response({"date": date_validation["message"]}, status=status.HTTP_400_BAD_REQUEST)
            
            self.perform_create(form.save())
            return Response(form, status=status.HTTP_201_CREATED)
        else:
            # Dados da requisição POST são inválidos
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

def schedulingForm(request):
    """
    View to render schedule template and verify the data 
    """
    #Take a list of available dates to schedule
    available_schedules = Schedule.search_for_available_dates(Schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        #Verify is form is valid
        if form.is_valid():
            form.save(commit=False) 
            #verify date
            date_validation = form.verify_date()
            #if date not valid return a error message to the template
            if not date_validation['valid']:
                context = {
                    'form': form, 
                    'date_error': date_validation['message'][0], #Inform to template if the date has already been scheduled
                    'available_schedules': available_schedules
                }
                return render(request, 'schedulingView.html', context)
            else: 
                #Save data on database
                schedule = form.save()
                context = {
                        'form': form, 
                        'success': 'success', #Inform to template if the schedule has been saved with success
                        'available_schedules': available_schedules
                    }
                #Send email to the client
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
