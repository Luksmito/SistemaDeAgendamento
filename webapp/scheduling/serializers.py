from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id','date', 'hour', 'name', 'email', 'healthInsurance', 'telephone')