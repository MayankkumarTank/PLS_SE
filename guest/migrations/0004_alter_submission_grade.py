# Generated by Django 3.2 on 2021-04-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0003_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='Grade',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
