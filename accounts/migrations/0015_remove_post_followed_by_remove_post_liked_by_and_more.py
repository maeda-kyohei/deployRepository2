# Generated by Django 4.1 on 2024-05-08 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_post_followed_by_post_liked_by_alter_post_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="followed_by",),
        migrations.RemoveField(model_name="post", name="liked_by",),
        migrations.AddField(
            model_name="notification",
            name="read",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2024, 5, 8, 21, 13, 5, 289166), null=True
            ),
        ),
    ]