# Generated by Django 4.2.6 on 2023-10-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора книги', to='catalog.author', verbose_name='Автор книги'),
        ),
    ]
