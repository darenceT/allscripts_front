# Generated by Django 4.0.2 on 2022-02-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='review_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
