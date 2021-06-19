from django.urls import path
from .views import (
    index,
    register,
    login_view,
    logout_view,
    create_meet,
    delete_meet,
    update_meet,
    update_profile
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create_meet/', create_meet, name='create_meet'),
    path('update_meet/<str:pk>/', update_meet, name='update_meet'),
    path('delete_meet/<str:pk>/', delete_meet, name='delete_meet'),
    path('update_profile/', update_profile, name='update_profile')
]