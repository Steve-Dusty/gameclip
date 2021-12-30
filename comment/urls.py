from django.urls import path
from django.shortcuts import render
from .views import CommentCreateView, CommentListView

urlpatterns = [
	path("comment/<int:pk>", CommentCreateView.as_view(), name="comment-create"),
	path('debug-comment', CommentListView.as_view(), name="comment-list")

]