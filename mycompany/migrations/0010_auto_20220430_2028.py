# Generated by Django 3.1 on 2022-04-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0009_auto_20220429_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('free', 'Free'), ('basic', 'Basic'), ('pro', 'Pro.')], max_length=10, null=True),
        ),
    ]
