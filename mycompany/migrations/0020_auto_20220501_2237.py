# Generated by Django 3.1 on 2022-05-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0019_auto_20220501_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('free', 'Free'), ('basic', 'Basic'), ('pro', 'Pro.')], max_length=10, null=True),
        ),
    ]