# Generated by Django 3.2.4 on 2021-10-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.TextField(blank=True, null=True, verbose_name='язык'),
        ),
    ]
