# Generated by Django 4.1.7 on 2023-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormHouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('img', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('low_img', models.TextField(default='')),
                ('high_img', models.TextField(default='')),
                ('type', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('floor_area', models.CharField(max_length=255)),
                ('plot_area', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('costs', models.TextField(default='')),
                ('vr_img', models.TextField(default='')),
                ('date_added', models.DateTimeField()),
            ],
            options={
                'db_table': 'form_houses',
            },
        ),
    ]
