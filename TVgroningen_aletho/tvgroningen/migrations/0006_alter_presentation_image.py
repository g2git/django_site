# Generated by Django 5.1.5 on 2025-02-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvgroningen', '0005_alter_presentation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
