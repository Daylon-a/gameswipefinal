# Generated by Django 4.0.3 on 2022-04-15 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecarousel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='gameno',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='rating',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]