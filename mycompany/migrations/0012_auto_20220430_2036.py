# Generated by Django 3.1 on 2022-04-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0011_auto_20220430_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('pro', 'Pro.'), ('free', 'Free'), ('basic', 'Basic')], max_length=10, null=True),
        ),
    ]