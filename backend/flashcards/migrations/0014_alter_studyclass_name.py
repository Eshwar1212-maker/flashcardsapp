# Generated by Django 4.2.8 on 2024-02-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0013_alter_flashcardset_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyclass',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]