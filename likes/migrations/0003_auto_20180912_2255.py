# Generated by Django 2.1.1 on 2018-09-12 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20180912_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecount',
            old_name='like_num',
            new_name='liked_num',
        ),
    ]
