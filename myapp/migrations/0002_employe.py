# Generated by Django 5.0.1 on 2024-01-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managerld', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=200, unique=True)),
                ('department', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=200)),
            ],
        ),
    ]
