# Generated by Django 2.1.5 on 2019-04-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wettkampf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ort', models.CharField(max_length=250)),
                ('Datum', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Wettkaempfe',
        ),
    ]
