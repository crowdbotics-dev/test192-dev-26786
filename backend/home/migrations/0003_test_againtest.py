# Generated by Django 2.2.28 on 2022-07-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="againtest",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
