from django.db import models
from datetime import datetime, time, date, timedelta
import typing
import holidays

HOUR_CHOICES = [
    ('7:00', '7:00'),
    ('8:00', '8:00'),
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
]

HEALTHINSURANCE_CHOICES = [
    ('Unimed', 'Unimed'),
    ('IPSEMG', 'IPSEMG')
]

class Schedule(models.Model):
    """
    Model to store schedule informations
    """
    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=50, blank=False, name='name', verbose_name='nome')
    date = models.DateField(blank=False, name='date', verbose_name='data')
    hour = models.TimeField(blank=False, name='hour', verbose_name='hora')
    email = models.EmailField(blank=False, name ='email', verbose_name='email')
    telephone = models.CharField(max_length=20, blank=False, name='telephone', verbose_name='telefone')
    healthInsurance = models.CharField(max_length=20,blank=True,default=None, name='healthInsurance',\
    verbose_name='convenio', choices=HEALTHINSURANCE_CHOICES)

    def __str__(self):
        return self.name

    def all_dates_scheduled(self) -> typing.List[datetime]:
        """
        This method return a list with all the schedule stored 
        """
        datas = self.objects.values_list('date', 'hour')
        datas = [datetime.combine(data[0], data[1]) for data in datas]
        return datas


    def next_date(hours: typing.List[time], actual: datetime) -> datetime:
        """
        Auxiliar function which receive a list of allowed hours to be scheduled and the 
        actual datetime and returns the next datetime that could be scheduled after the actual

        Args:
            hours (time): a list with the times which are allowed to be scheduled 
            actual (datetime): the actual time which you want to know what is the next time allowed 
        
        Returns:
            datetime: the next allowed datetime
        """
        weekdays = [i for i in range(0,7)]
        for hour in hours:
            if hour > actual.time():
                actual = actual.replace(hour=hour.hour, minute=hour.minute, second=0, microsecond=0)
                return actual
        new = actual + timedelta(days=1)
        while not (new.weekday() in weekdays):
            new = new + timedelta(days=1)
        new_time = time(hour=hours[0].hour, minute=hours[0].minute, second=0, microsecond=0)
        new = datetime.combine(new.date(), new_time)
        return new

    def search_for_available_dates(self) -> typing.List[datetime]:
        """
        Method which returns a list of the next ten dates available to schedule

        """
        hours = [time(7), time(8), time(9), time(10), time(11), time(13), time(14), time(15), time(16), time(17)]
        scheduled = self.all_dates_scheduled(self)
        actual = datetime.now()
        dates_available = []

        while len(dates_available) < 10:
            actual = self.next_date(hours, actual)
            if actual not in scheduled:
                dates_available.append(actual)
        return dates_available



class DateAdmin(models.Model):
    date = models.DateField(blank=False, name='date')

    def __str__(self):
        return str(self.date)

