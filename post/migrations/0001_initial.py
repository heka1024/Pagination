# Generated by Django 3.2.11 on 2022-01-15 16:35

from django.db import migrations, models
import enumfields.fields
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=25)),
                ("content", models.TextField()),
                (
                    "status",
                    enumfields.fields.EnumField(
                        default="draft", enum=post.models.Status, max_length=10
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
