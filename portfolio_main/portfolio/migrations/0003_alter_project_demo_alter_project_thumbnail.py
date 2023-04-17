# Generated by Django 4.2 on 2023-04-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_demo_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo',
            field=models.FileField(upload_to='portfolio/media/demos/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to='portfolio/media/thumbnails/'),
        ),
    ]
