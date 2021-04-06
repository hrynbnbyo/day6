from django.urls import path

from user import views

urlpatterns = [
    path("users/", views.AdminAPIView.as_view()),
    path("users/<str:id>/", views.AdminAPIView.as_view()),
]
