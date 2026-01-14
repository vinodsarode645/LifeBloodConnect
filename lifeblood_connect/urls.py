from django.contrib import admin
from django.urls import path
from bloodapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/register-donor/', views.register_donor, name='register_donor'),
    path('api/request-blood/', views.request_blood, name='request_blood'),
]