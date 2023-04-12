from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("delete/", views.delete, name="delete"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
    path("profile/<username>/", views.profile, name="profile"),
    # profile/<str:username>/ , str은 생략해도 str로 인식
    path("<int:user_pk>/follow/", views.follow, name="follow"),
]
