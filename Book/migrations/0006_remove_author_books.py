# Generated by Django 5.1.6 on 2025-02-20 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_author_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
    ]
