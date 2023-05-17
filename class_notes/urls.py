from django.urls import path
from class_notes.views import show_note
from class_notes.views import create_note
from class_notes.views import show_xml, show_json
app_name = 'class_notes'

urlpatterns = [
    path('', show_note, name='show_note'),
    path('create', create_note, name='create_note'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_xml, name='show_json'), 
]
