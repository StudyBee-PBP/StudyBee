from django.urls import path
from class_notes.views import show_note

app_name = 'class_notes'

urlpatterns = [
    path('', show_note, name='show_note'),
]
