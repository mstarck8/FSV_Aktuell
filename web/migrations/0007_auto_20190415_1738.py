# Generated by Django 2.1.5 on 2019-04-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190415_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wettkampf',
            name='Datum',
            field=models.DateField(),
        ),
    ]
