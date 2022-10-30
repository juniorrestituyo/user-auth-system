from django.urls import path
from . import views

urlpatterns = [
    path('loged/', views.loged, name='loged'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]