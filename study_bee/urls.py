from django.urls import path
from study_bee.views import show_planner, login_user, register, logout_user, add_plan, edit_plan, delete_plan, show_json, show_json_by_id #sesuaikan dengan nama fungsi yang dibuat



app_name = 'study_bee'

urlpatterns = [
    path('', show_planner, name='planner'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('planner/', show_planner, name='show_planner'),
    path('planner/add_plan/', add_plan, name='add_plan'),
    path('planner/edit_plan/<int:plan_id>/', edit_plan, name='edit_plan'),
    path('planner/delete_plan/<int:plan_id>/', delete_plan, name='delete_plan'),
    path('json/', show_json, name='show_json'),
    path('jsonbyid/<int:id>', show_json_by_id, name='show_json_by_id'),
]
