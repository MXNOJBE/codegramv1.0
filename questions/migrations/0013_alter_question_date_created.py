# Generated by Django 4.1.7 on 2023-04-11 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_alter_question_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 8, 52, 25, 16290, tzinfo=datetime.timezone.utc)),
        ),
    ]
