# Generated by Django 3.2.8 on 2021-10-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_remove_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is Account Verified'),
        ),
    ]