# Generated by Django 4.1.7 on 2023-02-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_alter_teammember_type_of_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateField(),
        ),
    ]
