# Generated by Django 4.1.7 on 2023-02-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='type_of_member',
            field=models.CharField(choices=[('MAN', 'Manager'), ('COACH', 'Coach'), ('P', 'Player'), ('CAP', 'Captain')], default='P', max_length=10),
        ),
    ]