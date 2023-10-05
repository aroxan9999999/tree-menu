from django.urls import path
from . import views

urlpatterns = [
    path('draw_menu/<str:menu_name>/', views.draw_menu, name='draw_menu'),
    path('my_page/<str:menu_name>/', views.my_page, name='my_page'),
]
