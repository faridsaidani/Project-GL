# Generated by Django 4.1.5 on 2023-01-27 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_addresse_alter_user_phonenumber"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="phoneNumber", new_name="phonenumber",
        ),
    ]
