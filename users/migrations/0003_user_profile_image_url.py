# Generated by Django 3.2.5 on 2022-01-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_birthday_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image_url',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]