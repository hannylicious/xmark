# Generated by Django 4.2.8 on 2024-01-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmarks', '0002_rename_is_favorite_bookmark_favorite_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='xmarks.tag'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
