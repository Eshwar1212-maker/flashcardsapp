# Generated by Django 4.2.8 on 2024-02-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0010_alter_flashcardset_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcardset',
            name='description',
            field=models.TextField(blank=True, max_length=40),
        ),
    ]