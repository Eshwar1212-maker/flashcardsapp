from .views import StudyClassView
from .views import FlashCardSetView, FlashCardView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('study-classes/', StudyClassView.as_view(), name='study-class'),
    #This endpoint can be hit with either the users id to GET all the study classes for that user, or a specific Study Class id to PATCH that study class
    path('study-classes/<str:user_id_or_study_class_id>/', StudyClassView.as_view(), name='study-class-update'),
    path('study-classes/<int:study_class_id>/flashcard-sets/', FlashCardSetView.as_view(), name='flashcard-set-list'),
    path('study-classes/<int:study_class_id>/flashcard-sets/<int:flashcard_set_id>/', FlashCardSetView.as_view(), name='flashcard-set-update'),
    path('study-classes/<int:flashcard_set_id>/flashcards/', FlashCardView.as_view(), name='flashcards'),
    path('flashcards/<int:flashcard_set_id>/flashcards/<int:flashcard_id>/', FlashCardView.as_view(), name='flashcard-detail'),
]
