from django.urls import path
from .import views
urlpatterns = [
     path('form/', views.user_form_view, name='user_form'),
]