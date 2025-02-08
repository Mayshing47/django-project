from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", auth_views.LoginView.as_view(template_name="first/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),  # Using built-in logout
    path("delete/<int:hobby_id>/", views.delete_hobby, name="delete_hobby"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
]


# from django.urls import path # type: ignore
# from . import views  
# from .views import delete_hobby
# from django.contrib.auth import views as auth_views  # import Django's auth view
# from .views import profile_view

# urlpatterns = [
#     path("", views.home, name="home"),  
#     path("about/", views.about, name="about"),  
#     path("login/", auth_views.LoginView.as_view(template_name="first/login.html"), name="login"),
#     path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
#     path('delete/<int:hobby_id>/', views.delete_hobby, name='delete_hobby'),
#     path("register/", views.register_view, name="register"),
#     path("profile/", profile_view, name="profile"),
# ]
