# Generated by Django 4.2.8 on 2024-02-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0006_alter_studyclass_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studyclass',
            old_name='user_id',
            new_name='user_id_or_study_class_id',
        ),
    ]
