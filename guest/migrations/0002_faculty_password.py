# Generated by Django 3.2 on 2021-04-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
