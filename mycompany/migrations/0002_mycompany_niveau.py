# Generated by Django 3.1 on 2022-04-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('basic', 'Basic'), ('free', 'Free'), ('pro', 'Pro')], max_length=10, null=True),
        ),
    ]
