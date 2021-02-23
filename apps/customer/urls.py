from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfilePageView.as_view(), name='profile'),
    path('profile_update/', views.user_profile_update, name='profile_update')
]
