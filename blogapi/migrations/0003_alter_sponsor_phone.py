# Generated by Django 3.2.4 on 2021-08-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0002_sponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
