# Generated by Django 4.0.2 on 2022-03-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0010_project_alter_skill_imagenlugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]