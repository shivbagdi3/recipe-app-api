"""
Views for User api.
"""
from rest_framework import generics

from user.serializers import UserSerializers


class CreateUserView(generics.CreateAPIView):
    '''create a new user'''
    serializer_class = UserSerializers
