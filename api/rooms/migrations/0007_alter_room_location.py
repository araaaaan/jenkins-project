# Generated by Django 3.2.4 on 2021-07-15 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20210630_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.location'),
        ),
    ]
