# Generated by Django 4.0.4 on 2023-08-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_formhouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fkhouse',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='formhouse',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lyyskihouse',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='maklerhouse',
            name='price',
            field=models.IntegerField(),
        ),
    ]
