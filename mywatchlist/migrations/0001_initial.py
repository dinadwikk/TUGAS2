# Generated by Django 4.1 on 2022-09-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentMyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('tittle', models.TextField()),
                ('rating', models.FloatField()),
                ('release_date', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
