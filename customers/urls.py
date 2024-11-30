from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.my_view, name='login'), 
    path('home/', views.customer_home, name='home'),  
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_request/', views.add_service_request, name='add_service_request'),
    path('track_requests/', views.track_requests, name='track_requests'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
