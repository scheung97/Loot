# Generated by Django 2.1.5 on 2019-02-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='swiper',
            name='next_item',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]