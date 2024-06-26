from django.db import models
from django.utils.timezone import now

class StudyClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id_or_study_class_id = models.CharField(max_length=96)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FlashCardSet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    study_class = models.ForeignKey(StudyClass, related_name='sets', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FlashCards(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    flashcard_set = models.ForeignKey(FlashCardSet, related_name='flashcards', on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return f'{self.front} / {self.back}'
