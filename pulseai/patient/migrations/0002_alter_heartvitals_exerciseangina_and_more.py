# Generated by Django 5.0.6 on 2024-06-24 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartvitals',
            name='ExerciseAngina',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=255, verbose_name='Exercise Angima'),
        ),
        migrations.AlterField(
            model_name='heartvitals',
            name='FastingBS',
            field=models.CharField(choices=[('0', 'Less than or equal to 120'), ('1', 'More than to 120')], max_length=255, verbose_name='Fasting Blood Sugar(60-900)'),
        ),
        migrations.AlterField(
            model_name='heartvitals',
            name='MaxHR',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='heartvitals',
            name='Oldpeak',
            field=models.FloatField(verbose_name='Old Peak'),
        ),
        migrations.AlterField(
            model_name='heartvitals',
            name='RestingBP',
            field=models.IntegerField(verbose_name='Resting Blood Pressure(60-220)'),
        ),
        migrations.AlterField(
            model_name='heartvitals',
            name='RestingECG',
            field=models.CharField(choices=[('Normal', 'Normal'), ('ST', 'Having ST-T wave abnormality'), ('LVH', "Showing probable or definite left ventricular hypertrophy by Estes' criteria")], max_length=255, verbose_name='Resting ECG Condition'),
        ),
    ]
