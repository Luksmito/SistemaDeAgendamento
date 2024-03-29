# Generated by Django 3.2.16 on 2023-02-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('date', models.DateField(verbose_name='data')),
                ('hour', models.TimeField(choices=[('7:00', '7:30'), ('8:00', '8:30'), ('9:00', '9:30'), ('10:00', '10:30'), ('11:00', '11:30'), ('13:00', '13:30'), ('14:00', '14:30'), ('15:00', '15:30')], verbose_name='hora')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('telephone', models.CharField(max_length=20, verbose_name='telefone')),
                ('healthInsurance', models.CharField(blank=True, choices=[('Unimed', 'Unimed'), ('IPSEMG', 'IPSEMG')], default=None, max_length=20, verbose_name='convenio')),
            ],
        ),
    ]
