# Generated by Django 2.2.28 on 2022-07-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_test_againtest"),
    ]

    operations = [
        migrations.CreateModel(
            name="TEst123",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("test456", models.BigIntegerField()),
            ],
        ),
    ]
