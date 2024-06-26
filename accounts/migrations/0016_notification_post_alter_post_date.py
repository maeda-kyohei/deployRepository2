# Generated by Django 4.1 on 2024-05-08 22:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_remove_post_followed_by_remove_post_liked_by_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.post",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 5, 9, 7, 33, 0, 632322), null=True
            ),
        ),
    ]
