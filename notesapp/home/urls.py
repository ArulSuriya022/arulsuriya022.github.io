from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    # path('signup/smart/notes/',views.HomeView.as_view(), name='home'),
    path('signup/smart/notes/', views.LoginInterfaceView.as_view(), name='login'),
]