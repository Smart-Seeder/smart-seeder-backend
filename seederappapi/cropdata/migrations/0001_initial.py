# Generated by Django 5.0.4 on 2024-04-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(default='crop/default.jpeg', upload_to='crop/')),
            ],
        ),
    ]