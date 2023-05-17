from django.urls import path
from class_notes.views import show_note
from class_notes.views import create_note

app_name = 'class_notes'

urlpatterns = [
    path('', show_note, name='show_note'),
    path('create', create_note, name='create_note'),
]
