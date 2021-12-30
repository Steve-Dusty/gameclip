from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Comment
from video.models import Video




# Create your views here.

class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ['content']

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class CommentListView(ListView):
	model = Comment
	template_name = "debug-comment.html"
	context_object_name = "comments"

	def get_queryset(self):
		comments = Comment.objects.order_by('-id') 
		return comments 
		# 