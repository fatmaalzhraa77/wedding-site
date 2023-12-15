# Generated by Django 4.2.7 on 2023-12-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_dress_flower_photographer_venue_remove_cake_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cake',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='dress',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='flower',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='photographer',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]