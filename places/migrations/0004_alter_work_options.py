# Generated by Django 3.2.6 on 2021-08-25 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210818_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['title']},
        ),
    ]