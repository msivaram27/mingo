# Generated by Django 5.0.7 on 2024-09-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srrp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
