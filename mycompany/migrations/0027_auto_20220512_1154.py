# Generated by Django 3.1 on 2022-05-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0026_auto_20220512_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('free', 'Free'), ('pro', 'Pro.'), ('basic', 'Basic')], max_length=10, null=True),
        ),
    ]
