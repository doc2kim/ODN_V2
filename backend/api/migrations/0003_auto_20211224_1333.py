# Generated by Django 3.2.9 on 2021-12-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_turb_opendata_ntu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opendata',
            name='lat',
            field=models.FloatField(default='none'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='lng',
            field=models.FloatField(default='none'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='ntu',
            field=models.FloatField(default='none'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='oxy',
            field=models.FloatField(default='none'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='ph',
            field=models.FloatField(default='none'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='salt',
            field=models.FloatField(default='none'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='temp',
            field=models.FloatField(default='none'),
        ),
    ]
