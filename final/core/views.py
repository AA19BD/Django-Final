from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer,JournalSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Book,Journal

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def get_permissions(self):
        if self.action=='list':
            permission_classes=(IsAuthenticated,)
        else:
            permission_classes=(IsAdminUser,)
        return [permission() for permission in permission_classes]

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]