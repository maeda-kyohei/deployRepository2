# Generated by Django 4.1 on 2024-05-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_post_pinned"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="duedate", field=models.DateField(null=True),
        ),
    ]