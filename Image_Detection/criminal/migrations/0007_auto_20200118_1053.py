# Generated by Django 3.0.1 on 2020-01-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminal', '0006_auto_20200117_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='photo',
            field=models.ImageField(default='criminal_pic_folder/None/no-img.jpg', upload_to='criminal_pic_folder/'),
        ),
    ]
