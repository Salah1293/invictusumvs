from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='login_user'),
    path('api/logout/', views.logout_user, name='logout_user'),
    path('api/roles_list/', views.role_list, name='role_list'),
    path('api/get_role/<str:pk>/', views.get_role, name='get_role'),
    path('api/update_role/<str:pk>/', views.update_role, name='update_role'),
    path('api/create_role/', views.create_role, name='create_role'),
    path('api/delete_role/<str:pk>/', views.delete_role, name='delete_role'),
]