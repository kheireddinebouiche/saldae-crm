# Generated by Django 3.1 on 2022-01-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
                ('response', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Foire aux question',
                'verbose_name_plural': 'Foire aux question',
            },
        ),
    ]
