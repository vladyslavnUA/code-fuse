from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('profiles/<int:pk>/update-profile/', views.ProfileUpdate.as_view(),
         name="update-profile"),
    path('profiles/<int:pk>/', views.UserProfile.as_view(), name="user-profile"),
]

# FOR PASSWORD RESET: https://medium.com/@khansubhan95/password-reset-in-django-8b4d37924958
# or https://learndjango.com/tutorials/django-password-reset-tutorial