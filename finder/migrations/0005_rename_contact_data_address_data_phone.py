# Generated by Django 4.0.2 on 2022-02-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_alter_data_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='contact',
            new_name='address',
        ),
        migrations.AddField(
            model_name='data',
            name='phone',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
