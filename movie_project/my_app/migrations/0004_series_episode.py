# Generated by Django 4.2.5 on 2023-10-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='episode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
