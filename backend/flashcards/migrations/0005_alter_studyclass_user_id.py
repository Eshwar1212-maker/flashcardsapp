# Generated by Django 4.2.8 on 2024-02-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_remove_studyclass_supabase_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyclass',
            name='user_id',
            field=models.CharField(),
        ),
    ]