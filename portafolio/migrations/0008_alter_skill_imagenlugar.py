# Generated by Django 4.0.2 on 2022-02-20 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0007_alter_skill_imagenlugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='imagenlugar',
            field=models.ImageField(upload_to='media\\images'),
        ),
    ]
