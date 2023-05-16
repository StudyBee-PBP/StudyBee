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
    path('json-answer/<int:id>', get_replies_json, name='get_replies_json'),
    path('delete-replies/<int:id>', delete_replies, name='delete_replies')

]