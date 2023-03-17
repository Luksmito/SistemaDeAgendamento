from django import forms
from django.core.exceptions import ValidationError
import holidays
from datetime import timedelta, date
from .models import Schedule, DateAdmin

class ScheduleForm(forms.ModelForm):
  """Class which will handle the Schedule form"""
  hour = forms.ChoiceField(choices=[
    ('7:00', '7:00'),
    ('8:00', '8:00'),
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
], label="Hora")
  class Meta:
      model = Schedule
      fields = ['date', 'hour', 'name', 'email', 'healthInsurance', 'telephone']
      widgets = {
        'date': forms.DateInput(attrs={'placeholder': "dia/mes/ano", 'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'}),
        'telephone': forms.TextInput(attrs={'class': 'form-control'})
      }
        

  def verify_date(self):
    """Method to verify if the date saved in form has already been scheduled
       Return: 
       bool: True if the date has already scheduled, False if don't
    """
    cleaned_data = super().clean()
    date = cleaned_data.get('date')
    hour = cleaned_data.get('hour')

    validation = {
      'valid': True,
      'message': []
    }

    if date in holidays.CountryHoliday('BR'): #Verify if date is a holiday
      validation['valid'] = False
      validation['message'].append('Essa data é um feriado')
    elif Schedule.objects.filter(date=date, hour=hour).exists() or DateAdmin.objects.filter(date=date).exists():
      validation['valid'] = False
      validation['message'].append('Essa data e hora ja tem agendamento')
    
    elif date < date.today():
      validation['valid'] = False
      validation['message'].append('A data deve ser futura')
    return validation
      

    

