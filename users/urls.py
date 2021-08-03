from django.urls import path
from users.views import UserLoginView, UserRegistrationView, logout, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]