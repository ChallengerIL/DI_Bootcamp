# Generated by Django 4.2.2 on 2023-06-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_share', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='uploads_number',
            new_name='uploads_count',
        ),
    ]
