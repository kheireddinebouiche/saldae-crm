# Generated by Django 3.1 on 2022-04-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0002_mycompany_niveau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('free', 'Free'), ('pro', 'Pro.'), ('basic', 'Basic')], max_length=10, null=True),
        ),
    ]