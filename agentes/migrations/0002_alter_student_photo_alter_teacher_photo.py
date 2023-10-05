# Generated by Django 4.2.6 on 2023-10-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to='photos/students/', verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='photos/teachers/', verbose_name='foto'),
        ),
    ]
