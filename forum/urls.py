from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', show_forum, name='show_forum'),
    path('create/', create_forum_ajax, name='create_forum'),
    path('add-replies/<int:id>', add_replies_ajax, name='add_replies_ajax'),
    path('discussion/<int:id>', show_discussion, name='show_discussion'), 
    path('delete/<int:id>', delete_forum, name='delete_forum'),
    path('json-post/', get_post_json, name='json-post'),
    path('json-post/<int:id>', get_post_json_by_id, name='get_post_json_by_id'),
    path('json-post/<str:username>', get_post_json_by_username, name='get_post_json_by_username'),
    path('json-answer/<int:id>', get_replies_json, name='get_replies_json'),
    path('delete-replies/<int:id>', delete_replies, name='delete_replies'),
    path('create-flutter/', create_forum_flutter, name='create_forum_flutter'),
    path('add-replies-flutter/', add_replies_flutter, name='add_replies_flutter'),
    path('delete-flutter/<int:id>', delete_forum_flutter, name='delete_forum_flutter'),
    path('delete-replies-flutter/<int:id>', delete_replies_flutter, name='delete_replies_flutter'),
]