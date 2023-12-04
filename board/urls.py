from django.urls import path
from board import views
from board.views import association_map_view

app_name = "board"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("association-map/", association_map_view, name="association_map"),
]
