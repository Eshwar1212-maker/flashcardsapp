from django.db import models
from django.conf import settings

class StudyClass(models.Model): 
    supabase_user_id = models.UUIDField(default=0) 
    name = models.CharField(max_length = 50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FlashCardSet(models.Model):
    study_class = models.ForeignKey(StudyClass, related_name='sets', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class FlashCards(models.Model):
    flashcard_set = models.ForeignKey(FlashCardSet, related_name='flashcards', on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return f'{self.front} / {self.back}'