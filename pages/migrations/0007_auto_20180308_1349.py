# Generated by Django 2.0.2 on 2018-03-08 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_tasting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasting',
            options={'ordering': ['-tasting_date']},
        ),
    ]
