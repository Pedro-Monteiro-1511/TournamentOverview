# Generated by Django 4.1.7 on 2023-02-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_alter_match_match_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateField(default=0),
        ),
    ]
