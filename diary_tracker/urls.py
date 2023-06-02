from django.urls import path
from diary_tracker.views import create_diary_flutter, show_tracker
from diary_tracker.views import create_diary_ajax
from diary_tracker.views import modify_diary
from diary_tracker.views import delete_diary
from diary_tracker.views import show_xml 
from diary_tracker.views import show_json 
from diary_tracker.views import show_xml_by_id, show_json_by_id 

app_name = 'diary_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create-ajax/', create_diary_ajax, name='create_diary_ajax'),
    path('delete/<int:id>', delete_diary, name='delete_diary'),
    path('modify/<int:id>', modify_diary, name='modify_diary'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
    path('create-flutter/', create_diary_flutter, name='create_diary_flutter'),
]
