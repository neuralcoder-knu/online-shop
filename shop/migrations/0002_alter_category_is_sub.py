# Generated by Django 3.2.3 on 2024-05-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_sub',
            field=models.BooleanField(default=False),
        ),
    ]
