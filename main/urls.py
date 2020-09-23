from django.urls import path
from .views import employee_create_and_list_view

app_name = 'main'
urlpatterns = [
    path('', employee_create_and_list_view, name='main-post-view'),
]
