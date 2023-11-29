from django.urls import path
from board import views

app_name = "board"

urlpatterns =[
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]
