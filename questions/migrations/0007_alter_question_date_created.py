# Generated by Django 4.1.7 on 2023-03-28 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0006_alter_question_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 3, 28, 13, 50, 53, 277973, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
