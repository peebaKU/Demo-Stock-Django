from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datetime/', views.show_datetime, name='show_datetime'),
    path('tem/', views.my_template_view, name='my_template_view'),
    path('tem2/', views.my_template_view2, name='my_template_view2'),
]