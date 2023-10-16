# Generated by Django 4.2.1 on 2023-05-22 01:37

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos_teachers', verbose_name='foto')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('name', models.CharField(max_length=90, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('groups', models.ManyToManyField(related_name='classes_on_teachers', to='produtos.group', verbose_name='turmas')),
            ],
            options={
                'verbose_name': 'professore',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos_students', verbose_name='foto')),
                ('name', models.CharField(max_length=90, verbose_name='nome')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.course', verbose_name='curso')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.group', verbose_name='turma')),
            ],
            options={
                'verbose_name': 'estudante',
            },
        ),
    ]