# Generated by Django 4.0.2 on 2022-02-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0002_data_review_score_alter_data_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='contact',
            field=models.TextField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='years',
            field=models.CharField(default=0, max_length=100),
        ),
    ]