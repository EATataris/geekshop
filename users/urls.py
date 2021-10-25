from django.urls import path
from users.views import UserLoginView, UserRegistrationView, Logout, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activation_key>/', UserRegistrationView.verify, name='verify'),
]