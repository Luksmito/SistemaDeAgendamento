# Generated by Django 3.2.16 on 2023-02-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='hour',
            field=models.TimeField(choices=[('7:00', '7:00'), ('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00')], verbose_name='hora'),
        ),
    ]