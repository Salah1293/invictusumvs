from django.urls import path
from . import views



urlpatterns = [
    
    #SERVICES APIS ROUTS
    path('api/services_list/', views.services_list, name='services'),
    path('api/get_service/<int:pk>/', views.get_service, name='get_service'),
    path('api/create_service/', views.create_service, name='create_services'),
    path('api/update_service/<str:pk>/', views.update_service, name='update_service'),
    path('api/delete_service/<str:pk>/', views.delete_service, name='delete_service'),

    #MISSIONS APIS ROUTS
    path('api/missions_list/', views.missions_list, name='missions_list'),
    path('api/get_mission/<str:pk>/', views.get_mission, name='get_mission'),
    path('api/create_mission/', views.create_mission, name='create_mission'),
    path('api/update_mission/<str:pk>/', views.update_mission, name='update_mission'),
    path('api/delete_mission/<str:pk>/', views.delete_mission, name='delete_mission'),
    
]