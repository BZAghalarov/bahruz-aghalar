# Generated by Django 4.1 on 2022-08-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_alter_stoptimes_stop_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoptimes',
            name='arrival_time',
            field=models.CharField(max_length=100),
        ),
    ]