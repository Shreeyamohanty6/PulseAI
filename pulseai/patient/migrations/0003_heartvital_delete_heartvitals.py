# Generated by Django 5.0.6 on 2024-06-24 11:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_heartvitals_exerciseangina_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartVital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=255)),
                ('ChestPainType', models.CharField(choices=[('TA', 'Typical Angina'), ('ATA', 'Atypical Angina'), ('NAP', 'Non-Anginal Pain'), ('ASY', 'Asymptomatic')], max_length=255, verbose_name='Chest Pain Type')),
                ('RestingBP', models.IntegerField(verbose_name='Resting Blood Presure (60-220)')),
                ('Cholesterol', models.IntegerField()),
                ('FastingBS', models.CharField(choices=[('0', 'Less than or equal to 120'), ('1', 'More than to 120')], max_length=255, verbose_name='Fasting Blood Suger (60 - 900)')),
                ('RestingECG', models.CharField(choices=[('Normal', 'Normal'), ('ST', 'Having ST-T wave abnormality'), ('LVH', "Showing probable or definite left ventricular hypertrophy by Estes' criteria")], max_length=255, verbose_name='Resting ECG Condition')),
                ('MaxHR', models.IntegerField(verbose_name='Maximum Heart Rate (60 - 220)')),
                ('ExerciseAngina', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=255, verbose_name='Exercise Angina')),
                ('Oldpeak', models.FloatField(verbose_name='Oldpeak(-2.5 - +2.5)')),
                ('ST_Slope', models.CharField(choices=[('Flat', 'Flat'), ('Up', 'Upsloping'), ('Down', 'Downsloping')], max_length=255)),
                ('heart_disease', models.CharField(blank=True, max_length=255)),
                ('prediction_probability', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='HeartVitals',
        ),
    ]
