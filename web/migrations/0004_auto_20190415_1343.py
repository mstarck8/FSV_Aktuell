# Generated by Django 2.1.5 on 2019-04-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190414_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wettkampf',
            name='Datum',
            field=models.DateTimeField(),
        ),
    ]
