from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("todos/", views.TodoList.as_view()),
    path("todos/<int:pk>", views.TodoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)