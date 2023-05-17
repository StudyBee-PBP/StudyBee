from django.urls import path
from class_notes.views import show_note
from class_notes.views import create_note
from class_notes.views import show_xml, show_json
from class_notes.views import show_xml_by_id, show_json_by_id 
from class_notes.views import modify_note
from class_notes.views import delete_note

app_name = 'class_notes'

urlpatterns = [
    path('', show_note, name='show_note'),
    path('create', create_note, name='create_note'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_xml, name='show_json'), 
        
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
    
    path('modify/<int:id>', modify_note, name='modify_note'), 
    path('delete/<int:id>', delete_note, name='delete_note'), 


]
