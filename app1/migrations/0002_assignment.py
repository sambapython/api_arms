# Generated by Django 4.0 on 2024-03-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('floor', models.CharField(max_length=250)),
                ('resources', models.CharField(max_length=250)),
            ],
        ),
    ]
