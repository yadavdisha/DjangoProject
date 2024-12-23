from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path("templates/", views.print_hello_template),
     path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
     path('all_data/', views.all_data),
     path("sud/<int:pk>/",views.single_user_data)
]

