# Generated by Django 4.2.1 on 2023-05-30 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsbaikal', '0007_alter_question_changed_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='changed_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 20, 8, 32, 822860, tzinfo=datetime.timezone.utc), verbose_name='date changed'),
        ),
        migrations.AlterField(
            model_name='question',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 20, 8, 32, 822840, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
