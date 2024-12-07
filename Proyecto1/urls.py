from django.contrib import admin
from django.urls import path, include
from AppCoder import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appcoder/', include('AppCoder.urls')),
    path('', views.index, name='home'), 
]
