# Generated by Django 4.0.3 on 2022-03-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.IntegerField(default=0, verbose_name='Кол-во комминтариев'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='image_1.jpg', upload_to='', verbose_name='Фото'),
        ),
    ]
