# Generated by Django 3.1.3 on 2021-05-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forminp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='contact',
            field=models.CharField(max_length=11),
        ),
    ]
