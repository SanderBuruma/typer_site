# Generated by Django 4.1 on 2022-08-24 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookChapter',
            new_name='Chapter',
        ),
        migrations.RenameModel(
            old_name='PartLine',
            new_name='Line',
        ),
        migrations.RenameModel(
            old_name='ChapterPart',
            new_name='Section',
        ),
    ]
