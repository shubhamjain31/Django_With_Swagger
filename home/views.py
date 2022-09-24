from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class ListTodoAPIView(ListAPIView):
    """Lists all todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields    = ['id', 'title']
    search_fields       = ['title', 'body']
    ordering_fields     = ['id']

class CreateTodoAPIView(CreateAPIView):
    """Creates a new todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    """Update the todo whose id has been passed through the request"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """Deletes a todo whose id has been passed through the request"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer