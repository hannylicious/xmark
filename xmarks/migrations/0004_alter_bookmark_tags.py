# Generated by Django 4.2.8 on 2024-01-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmarks', '0003_remove_bookmark_category_remove_tag_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, to='xmarks.tag'),
        ),
    ]