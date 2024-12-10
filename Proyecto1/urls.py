from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from AppCoder import views  
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('AppCoder.urls')), 
    path('login/', auth_views.LoginView.as_view(next_page='/profile/'), name='login'),
    path('register/', views.register, name='register'),  
    path('profile/', views.profile, name='profile'),  
]
