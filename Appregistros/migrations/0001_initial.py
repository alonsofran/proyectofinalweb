# Generated by Django 4.1.3 on 2023-01-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
