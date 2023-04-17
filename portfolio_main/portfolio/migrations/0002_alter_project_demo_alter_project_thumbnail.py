# Generated by Django 4.2 on 2023-04-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo',
            field=models.FileField(upload_to='portfolio/media/portfolio/demos'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to='portfolio/media/portfolio/thumbnails'),
        ),
    ]
