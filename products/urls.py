from django.urls import path
from . import views



urlpatterns = [
    #ROBOT TYPES ROUTS
    path('api/robot_type_list/', views.robot_type_list, name='robot_type_list'),
    path('api/get_robot_type/<str:pk>/', views.get_robot_type, name='robot_type'),
    path('api/create_robot_type/', views.create_robot_type, name='create_robot_type'),
    path('api/update_robot_type/<str:pk>/', views.update_robot_type, name='update_robot_type'),
    path('api/delete_robot_type/<str:pk>/', views.delete_robot_type, name='delete_robot_type'),
    #ROBOT ROUTS
    path('api/robot_list/', views.robot_list, name='robot_list'),
    path('api/get_robot/<str:pk>/', views.get_robot, name='robot'),
    path('api/update_robot/<str:pk>/', views.update_robot, name='update_robot'),
    path('api/create_robot/', views.create_robot, name='create_robot'),
    path('api/delete_robot/<str:pk>/', views.delete_robot, name='delete_robot'),
    #COMPONENT TYPES ROUTS
    path('api/component_type_list/', views.component_type_list, name='component_type_list'),
    path('api/get_component_type/<str:pk>/', views.get_component_type, name='component_type'),
    path('api/update_component_type/<str:pk>/', views.update_component_type, name='update_component_type'),
    path('api/create_component_type/', views.create_component_type, name='create_component_type'),
    path('api/delete_component_type/<str:pk>/', views.delete_component_type, name='delete_component_type'),
    #COMPONENT MODEL ROUTS
    path('api/component_model_list/', views.component_model_list, name='component_model_list'),
    path('api/get_component_model/<str:pk>/', views.get_component_model, name='component_model'),
    path('api/create_component_model/', views.create_component_model, name='create_component_model'),
    path('api/update_component_model/<str:pk>/', views.update_component_model, name='update_component_model'),
    path('api/delete_component_model/<str:pk>/', views.delete_component_model, name='delete_component_model'),
    #ROBOT STATUS ROUT
    path('api/robot_statuses/', views.list_robot_statuses, name='list_robot_statuses'),
     
]