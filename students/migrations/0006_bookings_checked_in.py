# Generated by Django 4.0 on 2022-09-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_book_checked_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='checked_in',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
