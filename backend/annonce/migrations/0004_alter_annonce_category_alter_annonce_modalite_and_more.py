# Generated by Django 4.1.5 on 2023-01-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("annonce", "0003_rename_theme_annonce_theme_remove_annonce_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="annonce",
            name="category",
            field=models.CharField(
                choices=[
                    ("primaire", "primaire"),
                    ("college", "college"),
                    ("lycee", "lycee"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="annonce",
            name="modalite",
            field=models.CharField(
                choices=[("offline", "offline"), ("online", "online")], max_length=8
            ),
        ),
        migrations.AlterField(
            model_name="annonce",
            name="theme",
            field=models.CharField(
                choices=[("math", "math"), ("science", "science")], max_length=50
            ),
        ),
    ]
