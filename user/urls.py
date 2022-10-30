from django.urls import path
from . import views

urlpatterns = [
    path('logged/', views.logged, name='logged'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup')
]