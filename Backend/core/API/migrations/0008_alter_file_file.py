# Generated by Django 4.1.6 on 2023-02-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
