from django.urls import path, include
from . import views


app_name = 'trial'

urlpatterns = [
    path('api/<str:model>', views.api_handler, name='api'),
    path('api/<str:model>/<int:pk>', views.api_handler, name='api'),
    path('api/', views.api_handler, name='api'),
]
