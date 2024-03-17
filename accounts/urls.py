from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('profile', views.UserView.as_view(), name='profile_view'),
    path('register', views.UserRegisterView.as_view(), name='register_view'),
    path('useradlist', views.UserAdListView.as_view(), name='user_ad_list_view'),
]