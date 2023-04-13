# Generated by Django 4.1.7 on 2023-04-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authy", "0007_alter_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="company_email",
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="company_name",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_recruiter",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_student",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_user",
            field=models.BooleanField(default=False),
        ),
    ]
