# Generated by Django 4.1 on 2022-08-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_alter_routes_route_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stops',
            name='stop_desc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
