# Generated by Django 4.2.4 on 2023-08-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
